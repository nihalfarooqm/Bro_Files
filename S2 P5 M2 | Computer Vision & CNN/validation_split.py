import os
import random
import shutil

dataset_dir = "dataset"
split_ratio = 0.20  # Moves 20% to validation

for category in ["cats", "dogs"]:
    train_path = os.path.join(dataset_dir, "train", category)
    val_path = os.path.join(dataset_dir, "validation", category)

    os.makedirs(val_path, exist_ok=True)

    images = os.listdir(train_path)
    num_to_move = int(len(images) * split_ratio)
    selected = random.sample(images, num_to_move)

    for img in selected:
        shutil.move(os.path.join(train_path, img), os.path.join(val_path, img))

    print(
        f"Moved {num_to_move} images from train/{category} to validation/{category}."
    )
