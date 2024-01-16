# from cgitb import text
import sys
from pygame import mixer
from PyQt6.QtGui import QPixmap, QImage
from PyQt6 import QtWidgets, uic
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
        self.table_songs.itemSelectionChanged.connect(self.select_song)
        self.slider_volume.valueChanged.connect(self.volume_changer)
        self.btn_forward.clicked.connect(self.next)
        
    
    is_playing = False
    pause = False
    song_list = []
    current_song = ""
    song_path = []
    
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
            row = self.table_songs.rowCount()
            this_song =self.tag_extractor(open_file[song])
            this_song =self.tag_extractor(open_file[song])
            self.song_list.append(this_song["Path"])
            self.table_songs.insertRow(row)
            self.table_songs.setItem(row, 0, QTableWidgetItem(this_song['Artist']))
            self.table_songs.setItem(row, 1, QTableWidgetItem(str(this_song['Title'])))
            self.table_songs.setItem(row, 2, QTableWidgetItem(this_song['Album']))
            self.table_songs.setItem(row, 3, QTableWidgetItem(this_song['Length']))


    def back(self):
        open_file = list(QFileDialog.getOpenFileNames(caption="Open Song")[0])
        self.fill_list(open_file)
        if self.is_playing == False:
            self.current_song = self.song_list[0]
            self.play_pause()

    def next(self):
        self.current_song = self.song_list[self.table_songs.currentRow() + 2]
        print(self.current_song)
        self.is_playing = False
        mixer.music.load(self.current_song)
        mixer.music.play()
        # self.play_pause()

    
    def label_changer(self):
        a = self.tag_extractor(self.current_song)
        if self.is_playing == True:
            self.lbl_song.setText(str(a["Artist"]))
            self.lbl_artist.setText(str(a["Title"]))
        
    def select_song(self):
        mixer.music.stop()
        self.is_playing = False
        self.current_song = self.song_list[self.table_songs.currentRow()]
        self.play_pause()

    def tag_extractor(self, mysong):
        audio = ID3(mysong)
        song_artist = audio.get("TPE1").text[0]
        song_artwork = audio.get("APIC:")
        song_album = audio.get("TALB").text[0]
        song_length = audio.get("TLEN")
        song_path = mysong
        song_name = audio.get("TIT2")
        song_length = str(strftime("%M:%S", gmtime(MP3(mysong).info.length)))
        song_tags = {
            'Artist' : song_artist,
            'Album' : song_album,
            'Length' : song_length,
            'Artwork' : song_artwork,
            'Path' : song_path,
            "Title" : song_name,
            "Length" : song_length,
        }
        return song_tags

    def artwork(self):
        artwork = self.tag_extractor(self.current_song)['Artwork']
        pixmap = QPixmap()
        pixmap.loadFromData(artwork.data)
        self.lbl_artwork.setPixmap(pixmap)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()