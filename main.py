import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!", text_color="white")

    except:
        finishLabel.configure(text="Download Error!", text_color="red")



def mp3Download():
    try:
        mp3Link = mp3_Link.get()
        mp3Object = YouTube(mp3Link, on_progress_callback=on_progress)
        music = mp3Object.streams.get_audio_only()

        mp3_title.configure(text=mp3Object.title, text_color="white")
        mp3_finishLabel.configure(text="")
        music.download()
        mp3_finishLabel.configure(text="Downloaded!", text_color="white")
    except:
        mp3_finishLabel.configure(text="Download Error!", text_color="red")


# def mp3_on_progress(stream, chunk, bytes_remaining):
#     total_size = stream.filesize
#     bytes_downloaded = total_size - bytes_remaining
#     percentage_of_completion = bytes_downloaded / total_size * 100
#     per = str(int(percentage_of_completion))
#     mp3_pPercentage.configure(text=per + "%")
#     mp3_pPercentage.update()
#
#     # Update ProgressBar
#     progressBar.set(float(percentage_of_completion) / 100)




def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()



    # Update ProgressBar
    progressBar.set(float(percentage_of_completion) / 100)




# System Setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720×480")
app.title("Youtube Dowloader")

#Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert A Youtube Link ")
title.pack(padx=10, pady=10)

#Link Input
url_var = tkinter.StringVar()
link_title = customtkinter.CTkLabel(app, text="YouTube Video To Mp4")
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link_title.pack(padx= 10, pady = 10)
link.pack()

# Finished Dowloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress Percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 10, pady = 10)






# YT Video To Mp3
mp3_title = customtkinter.CTkLabel(app, text="")
mp3_title.pack(padx= 60, pady = 70)


mp3_title = customtkinter.CTkLabel(app, text="Insert A YouTube Link")
mp3_title.pack(padx= 10, pady = 10)

# Mp3 Link
mp3_url_var = tkinter.StringVar()
mp3_link_title = customtkinter.CTkLabel(app, text="YouTube Video To Mp3")

mp3_Link = customtkinter.CTkEntry(app,width=350, height=40, textvariable=mp3_url_var)
mp3_link_title.pack(padx= 10, pady = 10)
mp3_Link.pack()


# Mp3 Finished Dowloading
mp3_finishLabel = customtkinter.CTkLabel(app, text="")
mp3_finishLabel.pack()



# Mp3 Progress Percentage
# mp3_pPercentage = customtkinter.CTkLabel(app, text="0%")
# mp3_pPercentage.pack()
#
# mp3_progressBar = customtkinter.CTkProgressBar(app, width=400)
# mp3_progressBar.set(0)
# mp3_progressBar.pack(padx=10, pady=10)




# Mp3 Download Button
mp3_dButton = customtkinter.CTkButton(app, text="Download", command=mp3Download)
mp3_dButton.pack(padx= 10, pady = 10)



#Run App
app.mainloop()