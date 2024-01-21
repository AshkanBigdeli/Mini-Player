from pygame import mixer
from PyQt6.QtGui import QPixmap, QImage
from PyQt6 import QtWidgets, uic, QtGui
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QFileDialog, QTableWidgetItem
from PIL import ImageTk, Image
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
import io, easygui, random, sys, os
from ui import main
from time import strftime, gmtime

class MainWindow(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        mixer.init()
        self.setWindowTitle("--- Mini Player ---")
        self.setMinimumHeight(700)
        self.setMinimumWidth(650)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_slider_position)
        self.btn_playpause.clicked.connect(self.play_pause)
        self.btn_stop.clicked.connect(self.stop)
        self.btn_open_file.clicked.connect(self.open_file)
        self.table_songs.itemDoubleClicked.connect(self.select_song)
        self.slider_volume.valueChanged.connect(self.volume_changer)
        self.btn_forward.clicked.connect(self.next)
        self.btn_back.clicked.connect(self.prev)
        self.btn_shuffle.clicked.connect(self.shuffle)
        self.horizontalSlider.sliderPressed.connect(self.seek_select)
    
    is_playing = False
    pause = False
    song_list = []
    current_song = ""
    song_path = []
    slider_current_position = 0
    
    def initial_slider(self):
        self.horizontalSlider.setValue(0)
        
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
                current_song_duration = self.get_sec(self.song_list[self.table_songs.currentRow()]['duration'])
                print(current_song_duration)
                self.horizontalSlider.setMaximum(current_song_duration) #set HorizontalSlider Maximum Value = current song duration
                self.timer.start(1000) #set timer to every 100 ms update the horizontal slider

            elif self.pause == True:
                mixer.music.unpause()
                self.pause = False
                self.is_playing = True
                self.timer.start(1000)
                self.btn_playpause.setText("Pause")

            else:
                mixer.music.pause()
                self.pause = True
                self.is_playing = False
                self.timer.stop()
                self.btn_playpause.setText("Play")

    def stop(self):
        if self.is_playing == False:
            pass
        else:
            mixer.music.stop()
            self.is_playing = False
            self.timer.stop()
            self.initial_slider()
    
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

    def open_file(self):
        open_file = list(QFileDialog.getOpenFileNames(caption="Open Song")[0])
        self.fill_list(open_file)
        if self.is_playing == False and self.pause == False:
            self.table_songs.selectRow(0)
            self.current_song = self.song_list[0]['path']
            self.play_pause()
            

    def next(self):
        self.initial_slider()
        if len(self.song_list) >1 :
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
        
    def prev(self):
        if len(self.song_list) > 1 :
            self.initial_slider()
            for item in self.song_list:
                if item['path'] == self.current_song:
                    current_row = self.song_list.index(item)
                    print(current_row)
                    break
            
            if current_row != 0: #back to the first row if on the last row
                self.current_song = self.song_list[current_row-1]['path']
                self.table_songs.selectRow(current_row-1)
            else:
                self.current_song = self.song_list[len(self.song_list)-1]['path']
                self.table_songs.selectRow(len(self.song_list)-1)           
            self.stop()
            self.play_pause()
    
    def label_changer(self):
        a = self.tag_extractor(self.current_song)
        if self.is_playing == True:
            self.lbl_song.setText(str(a["Artist"]))
            self.lbl_artist.setText(str(a["Title"]))
        
    def select_song(self):
        self.initial_slider()
        mixer.music.stop()
        self.is_playing = False
        selected_row = self.table_songs.currentRow()
        self.current_song = self.song_list[selected_row]['path']
        self.play_pause()

    def seek_select(self):
        current_row = self.table_songs.currentRow()
        seek_value = self.song_list[current_row]['duration']
        mixer.music.set_pos((self.horizontalSlider.value()))#*(self.get_sec(seek_value)))/100)
        self.horizontalSlider.setValue(int((self.horizontalSlider.value())))#*(self.get_sec(seek_value)))/100))

    def get_sec(self, time_str):
        """Get seconds from time."""
        m, s = time_str.split(':')
        return int(m) * 60 + int(s)

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

    def shuffle(self):
        if len(self.song_list) > 1:
            self.initial_slider()
            rnd = random.randint(0, len(self.song_list)-1)
            if rnd == self.table_songs.currentRow():
                rnd = rnd + 1
            self.current_song = self.song_list[rnd]['path']
            self.stop()
            self.play_pause()
            self.table_songs.selectRow(rnd)

    def update_slider_position(self):
        self.slider_current_position = 0
        self.slider_current_position += self.horizontalSlider.value() + 1
        print(self.slider_current_position)
        self.horizontalSlider.setValue(self.slider_current_position)

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