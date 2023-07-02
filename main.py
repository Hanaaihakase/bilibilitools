from download import *
from sessdata import *
from cid import *

if __name__ == "__main__":
    # Try to load sessdata from local file 
    sessdata = load_sessdata()
    # if the sessdata dont exist, get it from input
    if not sessdata:
        sessdata = input("Please input your sessdata:")
        # save the sessdata to local file 
        save_sessdata(sessdata)

    try:
        print("Select an option:")
        print("1. Get bvid from input")
        print("2. Get bvid from txt")
        option_choice = int(input("Enter an bvid: "))

        if option_choice == 1:
            # Get user input for bvid
            bvid = input("Please input your bvid:")
            for page in list(range(0, get_max_page(bvid))):
                download_audio(bvid, page, sessdata)

        elif option_choice == 2:
            # Get options from txt
            file_path = input("Enter the file path: ")

            bvids = []
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    bvid = line.strip()
                    bvids.append(bvid)
            for bvid in bvids:
                for page in list(range(0, get_max_page(bvid))):
                    download_audio(bvid, page, sessdata)

        else:
            raise ValueError("Invalid option number.")

    except ValueError as e:
        print(e)

