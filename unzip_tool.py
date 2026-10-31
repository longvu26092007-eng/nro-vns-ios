import zipfile
import os

zip_path = "NRO_VNS_Xcode.zip"
out_dir = "xcode_project"

with zipfile.ZipFile(zip_path, "r") as z:
    for m in z.infolist():
        clean = m.filename.replace("\\", "/").strip("/")
        if not clean:
            continue
        dst = os.path.join(out_dir, clean)
        if m.is_dir() or m.filename.endswith("/") or m.filename.endswith("\\"):
            os.makedirs(dst, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with z.open(m) as src, open(dst, "wb") as out:
                out.write(src.read())

print("Unzip completed successfully!")
