import glob

from PIL import Image

while True:
    try:
        dur = int(input("image duration(example 50,100,150): "))
        break
    except:
        print("please only put digits!")
def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.JPG")]
    frame_one = frames[0]
    frame_one.save("my_awesome.gif", format="GIF", append_images=frames,
                   save_all=True, duration=dur, loop=0)


if __name__ == "__main__":
    make_gif("your/jpg/folder")