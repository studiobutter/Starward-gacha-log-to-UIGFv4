import json
import os

def convert_source_to_target(source_path, target_path):
    with open(source_path, 'r') as source_file:
        source_data = json.load(source_file)

    target_data = {
        "info": {
            "export_timestamp": source_data["info"]["export_timestamp"],
            "export_app": "Starward Sleepy Converter (hk4e)",
            "export_app_version": "v1.0",
            "version": "v4.0"
        },
        "hk4e": [
            {
                "uid": source_data["info"]["uid"],
                "timezone": source_data["info"]["region_time_zone"],
                "list": []
            }
        ]
    }

    for item in source_data["list"]:
        target_item = {
            "id": item["id"],
            "uigf_gacha_type": item["uigf_gacha_type"],
            "gacha_type": item["gacha_type"],
            "item_id": item["item_id"],
            "time": item["time"],
            "rank_type": item["rank_type"]
        }
        target_data["hk4e"][0]["list"].append(target_item)

    source_filename = os.path.splitext(os.path.basename(source_path))[0]
    target_filename = f"UIGFv4_{source_filename}.json"
    if os.path.isdir(target_path):
        target_path = os.path.join(target_path, target_filename)
    else:
        target_path = target_filename

    with open(target_path, 'w') as target_file:
        json.dump(target_data, target_file, indent=4)

if __name__ == "__main__":

    source_path = input("Enter the source file: ").strip()
    target_path = input("Enter the target path (leave empty to save in the current directory): ").strip()
    if not target_path:
        target_path = "."

    if not os.path.isfile(source_path):
        print(f"Source file '{source_path}' does not exist.")
    else:
        convert_source_to_target(source_path, target_path)
        print(f"Conversion completed. Target file saved at '{target_path}'.")
