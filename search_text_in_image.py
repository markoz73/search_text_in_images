import functions

# lists file paths with searched string
while True:
    search_text = input('What text are are looking for? ')
    folder_path = functions.ask_folder()
    list_of_images = functions.list_files(folder_path)

    for image in list_of_images:
        text = functions.read_image(image).lower()
        if search_text.lower() in text:
            print(image)
    print("_" * 35)

