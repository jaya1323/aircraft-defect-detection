import os
import random
import shutil

images_dir = "images"
labels_dir = "labels"

base_dir = "dataset"
train_img = os.path.join(base_dir, "images/train")
val_img = os.path.join(base_dir, "images/val")
train_lbl = os.path.join(base_dir, "labels/train")
val_lbl = os.path.join(base_dir, "labels/val")

for path in [train_img, val_img, train_lbl, val_lbl]:
    os.makedirs(path, exist_ok=True)

images = [f for f in os.listdir(images_dir) if f.endswith((".jpg", ".png"))]

random.shuffle(images)

split_index = int(0.8 * len(images))
train_files = images[:split_index]
val_files = images[split_index:]

def move_files(file_list, img_dest, lbl_dest):
    for file in file_list:
        img_src = os.path.join(images_dir, file)
        lbl_src = os.path.join(labels_dir, file.replace(".jpg", ".txt").replace(".png", ".txt"))

        shutil.copy(img_src, os.path.join(img_dest, file))

        if os.path.exists(lbl_src):
            shutil.copy(lbl_src, os.path.join(lbl_dest, os.path.basename(lbl_src)))

move_files(train_files, train_img, train_lbl)
move_files(val_files, val_img, val_lbl)

print("✅ Dataset split complete!")
