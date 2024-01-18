# from cgitb import text
import sys, os
from pygame import mixer
from PyQt6.QtGui import QPixmap, QImage
from PyQt6 import QtWidgets, uic, QtGui
from PyQt6.QtWidgets import QFileDialog, QTableWidgetItem
from PIL import ImageTk, Image
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
import io, easygui
from ui import main
from time import strftime, gmtime

class MainWindow(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        mixer.init()
        self.setWindowTitle("--- Mini Player ---")
        self.btn_playpause.clicked.connect(self.play_pause)
        self.btn_stop.clicked.connect(self.stop)
        self.btn_back.clicked.connect(self.back)
        # self.table_songs.itemSelectionChanged.connect(self.select_song)
        self.table_songs.itemDoubleClicked.connect(self.select_song)
        self.slider_volume.valueChanged.connect(self.volume_changer)
        self.btn_forward.clicked.connect(self.next)
        
    
    is_playing = False
    pause = False
    song_list = []
    current_song = ""
    song_path = []
    list_counter = 0
    
    def volume_changer(self):
        mixer.music.set_volume(self.slider_volume.value()/100)
    
    def play_pause(self):
        
        if self.song_list == []:
            return
        else:
            self.artwork()
            if (self.is_playing == False and self.pause == False):
                mixer.music.load(self.current_song)
                mixer.music.play()
                self.is_playing = True
                self.btn_playpause.setText("Pause")
                self.label_changer()
                
            elif self.pause == True:
                mixer.music.unpause()
                self.pause = False
                self.is_playing = True
                self.btn_playpause.setText("Pause")

            else:
                mixer.music.pause()
                self.pause = True
                self.is_playing = False
                self.btn_playpause.setText("Play")
        
    def stop(self):
        if self.is_playing == False:
            pass
        else:
            mixer.music.stop()
            self.is_playing = False
    
    def fill_list(self, open_file):

        for song in range(len(open_file)):
            this_song =self.tag_extractor(open_file[song])
            song_dict = {
                "path": this_song['Path'],
                "title": this_song["Title"],
                "album": this_song["Album"],
                "artist": this_song["Artist"],
                "file_name" : this_song["File_Name"],
                # "artwork": this_song["Artwork"],
                "duration": this_song["Duration"],
            }
            if song_dict not in self.song_list:
                self.song_list.append(song_dict)
                
        self.table_songs.setRowCount(len(self.song_list))
        for i in range(len(self.song_list)):
            self.table_songs.setItem(i, 0, QTableWidgetItem(self.song_list[i]['artist']))
            self.table_songs.setItem(i, 1, QTableWidgetItem(str(self.song_list[i]['file_name'])))
            self.table_songs.setItem(i, 2, QTableWidgetItem(self.song_list[i]['album']))
            self.table_songs.setItem(i, 3, QTableWidgetItem(str(self.song_list[i]['duration'])))


    def back(self):
        open_file = list(QFileDialog.getOpenFileNames(caption="Open Song")[0])
        self.fill_list(open_file)
        if self.is_playing == False and self.pause == False:
            self.current_song = self.song_list[0]['path']
            self.play_pause()
            self.table_songs.selectRow(0)

    def next(self):
        for item in self.song_list:
            if item['path'] == self.current_song:
                current_row = self.song_list.index(item)
                break
        
        if current_row != len(self.song_list)-1: #back to the first row if on the last row
            self.current_song = self.song_list[current_row+1]['path']
            self.table_songs.selectRow(current_row+1)
        else:
            self.current_song = self.song_list[0]['path']
            self.table_songs.selectRow(0)
            
        self.stop()
        self.play_pause()

    
    def label_changer(self):
        a = self.tag_extractor(self.current_song)
        if self.is_playing == True:
            self.lbl_song.setText(str(a["Artist"]))
            self.lbl_artist.setText(str(a["Title"]))
        
    def select_song(self):
        mixer.music.stop()
        self.is_playing = False
        selected_row = self.table_songs.currentRow()
        self.current_song = self.song_list[selected_row]['path']
        self.play_pause()

    def tag_extractor(self, mysong):
        audio = ID3(mysong)
        song_artist = audio.get("TPE1").text[0]
        song_artwork = audio.get("APIC:")
        song_album = audio.get("TALB").text[0]
        song_duration = audio.get("TLEN")
        song_path = mysong
        file_name_without_path = os.path.basename(mysong)
        song_file_name = os.path.splitext(file_name_without_path)[0]
        song_name = audio.get("TIT2")
        song_duration = str(strftime("%M:%S", gmtime(MP3(mysong).info.length)))
        song_tags = {
            'Artist' : song_artist,
            'Album' : song_album,
            'Duration' : song_duration,
            'Artwork' : song_artwork,
            'Path' : song_path,
            "Title" : song_name,
            "File_Name" : song_file_name,
            
        }
        return song_tags

    def artwork(self):
        artwork = self.tag_extractor(self.current_song)['Artwork']
        if artwork is not None:
            pixmap = QPixmap()
            pixmap.loadFromData(artwork.data)
            self.lbl_artwork.setPixmap(pixmap)
        else:
            self.lbl_artwork.setPixmap(QtGui.QPixmap(":/icons/images/list-music.png"))


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()