import os

SOURCE = r"C:\Users\AADI\Yolo\benchmark\labels"
DEST = r"C:\Users\AADI\Yolo\benchmark_coco\labels"

os.makedirs(DEST, exist_ok=True)

mapping = {
    0: 0,  # person
    1: 2,  # car
    2: 5,  # bus
    3: 7,  # truck
    4: 3,  # motorcycle
    5: 1   # bicycle
}

for file in os.listdir(SOURCE):

    if not file.endswith(".txt"):
        continue

    src = os.path.join(SOURCE, file)
    dst = os.path.join(DEST, file)

    with open(src, "r") as fin, open(dst, "w") as fout:

        for line in fin:

            parts = line.strip().split()

            if len(parts) < 5:
                continue

            cls = int(parts[0])

            if cls in mapping:
                parts[0] = str(mapping[cls])
                fout.write(" ".join(parts) + "\n")

print("Done!")