import re
import xml.etree.ElementTree as ET
import random
import string
import uuid
import sys
from typing import List 

def get_id():
    return uuid.uuid4().hex


def convertChlidrenToAdvOutline(parents: List[ET.Element]):
    for outline in parents:
        if (outline.attrib["type"] == "outline"):
            convertToAdvancedOutline(outline)


def convertToAdvancedOutline(child: ET.Element):
    child.attrib['type'] = "advanced_outline"
    child.extend([ET.fromstring("""<param name="wplist">
    <wplist type="width_point" loop="false">
        <entry>
        <composite guid=\"""" + str(get_id()) + """\" type="width_point">
            <position>
            <real value="0.1000000000"/>
            </position>
            <width>
            <real value="1.0000000000"/>
            </width>
            <side_before>
            <integer value="0"/>
            </side_before>
            <side_after>
            <integer value="0"/>
            </side_after>
            <lower_bound>
            <real value="0.0000000000" static="true"/>
            </lower_bound>
            <upper_bound>
            <real value="1.0000000000" static="true"/>
            </upper_bound>
        </composite>
        </entry>
        <entry>
        <composite guid=\"""" + str(get_id()) + """\" type="width_point">
            <position>
            <real value="0.9000000000"/>
            </position>
            <width>
            <real value="1.0000000000"/>
            </width>
            <side_before>
            <integer value="0"/>
            </side_before>
            <side_after>
            <integer value="0"/>
            </side_after>
            <lower_bound>
            <real value="0.0000000000" static="true"/>
            </lower_bound>
            <upper_bound>
            <real value="1.0000000000" static="true"/>
            </upper_bound>
        </composite>
        </entry>
    </wplist>
    </param>"""), ET.fromstring("""    <param name="dash_enabled">
    <bool value="false"/>
    </param>"""), ET.fromstring("""    <param name="dilist">
    <dilist type="dash_item" loop="false">
        <entry>
        <composite guid=\"""" + str(get_id()) + """\" type="dash_item">
            <offset>
            <real value="0.1000000000"/>
            </offset>
            <length>
            <real value="0.1000000000"/>
            </length>
            <side_before>
            <integer value="4"/>
            </side_before>
            <side_after>
            <integer value="4"/>
            </side_after>
        </composite>
        </entry>
    </dilist>
    </param>"""), ET.fromstring("""    <param name="dash_offset">
    <real value="0.0000000000"/>
    </param>""")])
    for index, item in enumerate(list(child)):
        if (item.attrib["name"] == "sharp_cusps"):
            item.remove(list(item)[0])
            item.attrib["name"] = "cusp_type"
            integer = ET.SubElement(item, "integer").set("value", "0")
        if (item.attrib["name"] == "round_tip[0]"):
            item.remove(list(item)[0])
            integer = ET.SubElement(item, "integer").set("value", "1")
            item.attrib["name"] = "start_tip"
        if (item.attrib["name"] == "round_tip[1]"):
            item.remove(list(item)[0])
            ET.SubElement(item, "integer").set("value", "1")
            item.attrib["name"] = "end_tip"
        if (item.attrib["name"] == "homogeneous_width"):
            item.attrib["name"] = "homogeneous"
    pass


tree = ET.parse(sys.argv[1])
root = tree.getroot()
layers = root.findall(".//layer")


def findChildren(layers: ET.Element):
    for layer in layers:
        print(layer.attrib["desc"])
        if( layer.attrib['type'] == "group"):
            if(re.search("@.+", layer.attrib["desc"]) or re.search("@\*.+", layer.attrib["desc"]) ):
                shortMatch = True
            if (re.search("toAdvOutline\*_.+", layer.attrib["desc"]) or re.search("@\*.+", layer.attrib["desc"]) ):
                convertChlidrenToAdvOutline(layer.findall(".//layer"))
                if not shortMatch:
                    layer.attrib['desc'] = layer.attrib['desc'][14:]
                else:
                    layer.attrib['desc'] = layer.attrib['desc'][2:]
            if (re.search("toAdvOutline_.+", layer.attrib["desc"]) or re.search("@.+", layer.attrib["desc"])):
                findChildren(layer.findall(".//layer"))
                for param in layer.findall("param"):
                    convertChlidrenToAdvOutline(param[0].findall("layer"))
                if not shortMatch:
                    layer.attrib['desc'] = layer.attrib['desc'][13:]
                else:
                    layer.attrib['desc'] = layer.attrib['desc'][1:]
        if((re.search("toAdvOutline_.+", layer.attrib["desc"]) or re.search("@.+", layer.attrib["desc"])) and layer.attrib['type'] == "outline"):
            convertToAdvancedOutline(layer)
            if not shortMatch:
                layer.attrib['desc'] = layer.attrib['desc'][13:]
            else:
                layer.attrib["desc"] = layer.attrib["desc"][1:]


findChildren(layers)

tr2ee = ET.ElementTree(root)
if (len(sys.argv) == 3):
    outputFile = sys.argv[2]
else:
    outputFile = sys.argv[1]

with open(outputFile, "wb") as fh:
    tr2ee.write(fh)
