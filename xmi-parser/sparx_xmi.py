import xml.etree.ElementTree as ET
from yaml import safe_dump, SafeDumper
from re import fullmatch

# gen-markdown -d xmi-parser/md xmi-parser/USDM_UML_LINKML.yml
# gen-erdiagram xmi-parser/USDM_UML_LINKML.yml > xmi-parser/USDM_UML_MERMAID.md

xmi_file = "./Deliverables/UML/USDM_UML.xmi"
linkml_file = "./xmi-parser/USDM_UML_LINKML.yml"


ns = {
    "uml": "http://www.omg.org/spec/UML/20161101",
    "xmi": "http://www.omg.org/spec/XMI/20131001",
    "umldi": "http://www.omg.org/spec/UML/20161101/UMLDI",
    "dc": "http://www.omg.org/spec/UML/20161101/UMLDC",
}

root = ET.parse(xmi_file)
DEFAULT_RANGE = "string"
linkml = {
    "id": "https://cdisc.org/DDF/USDMUML",
    "name": "USDMUML",
    "prefixes": {"linkml": "https://w3id.org/linkml/"},
    "imports": ["linkml:types"],
    "default_range": DEFAULT_RANGE,
    "classes": {},
    "enums": {},
}


def get_name_by_id(id: str):
    custom = root.find(
        f".//uml:Model/packagedElement/packagedElement[@xmi:id='{id}']",
        ns,
    )
    primitive = root.find(
        f".//xmi:Extension/primitivetypes/packagedElement/packagedElement/packagedElement[@xmi:id='{id}']",
        ns,
    )
    target = custom or primitive
    return target.get("name")


def get_attribute(ownedAttribute: ET.Element):
    # TODO: how to handle Map and UUID?
    types = {
        "String": "string",
        "int": "integer",
        "Date": "date",
        "UUID": "string",
        "Map<String, String>": "string",
    }
    type = get_name_by_id(ownedAttribute.find("type", ns).get(f"{{{ns['xmi']}}}idref"))
    is_list = fullmatch(r"List<(.*)>", type)
    attribute = {}
    if is_list:
        type = is_list.group(1)
        attribute["multivalued"] = True
    type = types.get(type, type)
    if type != DEFAULT_RANGE:
        attribute["range"] = type
    if attribute != {}:
        return attribute


def get_class_properties(elt: ET.Element, cls: dict):
    for ownedAttribute in elt.findall("./ownedAttribute"):
        if ownedAttribute.get("name") not in cls:
            cls[ownedAttribute.get("name")] = get_attribute(ownedAttribute)


def get_enum_properties(elt: ET.Element, enum: dict):
    for ownedLiteral in elt.findall("./ownedLiteral"):
        enum[ownedLiteral.get("name")] = None


def get_classes():
    for element in root.findall(
        ".//uml:Model/packagedElement/packagedElement[@xmi:type='uml:Class']", ns
    ):
        linkml["classes"][element.get("name")] = {"attributes": {}}
        get_class_properties(
            element, linkml["classes"][element.get("name")]["attributes"]
        )


def get_enums():
    for element in root.findall(
        ".//uml:Model/packagedElement/packagedElement[@xmi:type='uml:Enumeration']", ns
    ):
        linkml["enums"][element.get("name")] = {"permissible_values": {}}
        get_enum_properties(
            element, linkml["enums"][element.get("name")]["permissible_values"]
        )


def main():
    get_classes()
    get_enums()
    SafeDumper.add_representer(
        type(None),
        lambda dumper, _: dumper.represent_scalar("tag:yaml.org,2002:null", ""),
    )
    with open(linkml_file, "w") as fp:
        safe_dump(linkml, fp, sort_keys=True)


if __name__ == "__main__":
    main()
