import os
import xml.etree.ElementTree as ET

xml_folder = "label"
output_folder = "labels"

os.makedirs(output_folder, exist_ok=True)

def convert(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (x * dw, y * dh, w * dw, h * dh)

for xml_file in os.listdir(xml_folder):
    if not xml_file.endswith(".xml"):
        continue

    tree = ET.parse(os.path.join(xml_folder, xml_file))
    root = tree.getroot()

    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    txt_path = os.path.join(output_folder, xml_file.replace(".xml", ".txt"))

    with open(txt_path, "w") as txt_file:
        for obj in root.iter("object"):

            xmlbox = obj.find("bndbox")

            xmin = float(xmlbox.find("xmin").text)
            xmax = float(xmlbox.find("xmax").text)
            ymin = float(xmlbox.find("ymin").text)
            ymax = float(xmlbox.find("ymax").text)

            bb = convert((w, h), (xmin, xmax, ymin, ymax))

            # FORCE CLASS = 0
            txt_file.write("0 " + " ".join(map(str, bb)) + "\n")
