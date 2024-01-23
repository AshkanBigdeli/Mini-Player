from pygame import mixer
from PyQt6.QtGui import QPixmap, QImage, QIcon
from PyQt6 import QtWidgets, uic, QtGui, QtCore
from PyQt6.QtCore import QTimer, QDir
from PyQt6.QtWidgets import QFileDialog, QTableWidgetItem
from PIL import ImageTk, Image
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
import io, easygui, random, sys, os
from ui import main
from time import strftime, gmtime
from datetime import timedelta

class MainWindow(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        mixer.init()
        self.setWindowTitle("--- Mini Player ---")
        self.setMinimumHeight(750)
        self.setMinimumWidth(650)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_slider_position)
        self.timer.timeout.connect(self.auto_next_play)
        self.btn_playpause.clicked.connect(self.play_pause)
        self.btn_stop.clicked.connect(self.stop)
        self.btn_open_file.clicked.connect(self.open_file)
        self.table_songs.itemDoubleClicked.connect(self.select_song)
        self.slider_volume.valueChanged.connect(self.volume_changer)
        self.btn_forward.clicked.connect(self.next)
        self.btn_back.clicked.connect(self.prev)
        self.btn_shuffle.clicked.connect(self.shuffle)
        self.horizontalSlider.sliderPressed.connect(self.seek_select)
        self.btn_playpause.setIcon(QIcon(QDir.current().filePath("ui/images/play.png")))
        self.btn_shuffle.setIcon(QIcon(QDir.current().filePath("ui/images/shuffle.png")))
        self.btn_shuffle.setIconSize(QtCore.QSize(30, 30))
        
    is_playing = False
    pause = False
    song_list = []
    current_song = ""
    song_path = []
    slider_current_position = 0

    def window_opacity(self):
        self.setWindowOpacity(0.8)

    def auto_next_track_finder(self):
        if self.table_songs.currentRow() != (len(self.song_list)-1):
            next_track = self.table_songs.currentRow()+1
        else:
            next_track = 0
    
        return next_track
        
    def set_slider_maximum(self):
        current_song_duration = self.get_sec(self.song_list[self.table_songs.currentRow()]['duration'])
        self.horizontalSlider.setMaximum(current_song_duration)
    
    def auto_next_play(self):
        if len(self.song_list) > 1:
            if self.horizontalSlider.value() >= self.horizontalSlider.maximum():
                self.initial_slider()
                mixer.music.queue(self.song_list[self.auto_next_track_finder()]['path'])
                self.table_songs.selectRow(self.auto_next_track_finder())
                self.current_song = self.song_list[self.table_songs.currentRow()]['path']
                self.set_slider_maximum()
                self.artwork()
                self.label_changer()
                
    def table_column_size(self):
        self.table_songs.horizontalHeader().setVisible(True)
        self.table_songs.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table_songs.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_songs.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_songs.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_songs.horizontalHeader().setStretchLastSection(False)
    
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
                self.btn_playpause.setIcon(QIcon(QDir.current().filePath("ui/images/pause.png")))
                self.label_changer()
                self.set_slider_maximum()
                self.timer.start(1000) #set timer to every 100 ms update the horizontal slider

            elif self.pause == True:
                mixer.music.unpause()
                self.pause = False
                self.is_playing = True
                self.timer.start(1000)
                self.btn_playpause.setIcon(QIcon(QDir.current().filePath("ui/images/pause.png")))

            else:
                mixer.music.pause()
                self.pause = True
                self.is_playing = False
                self.timer.stop()
                self.btn_playpause.setIcon(QIcon(QDir.current().filePath("ui/images/play.png")))

    def stop(self):
        if self.is_playing == False:
            pass
        else:
            mixer.music.stop()
            self.is_playing = False
            self.timer.stop()
            self.initial_slider()
            self.elapsed_time.setText("--:--")
            self.remaining_time.setText("--:--")
            self.lbl_artwork.setPixmap(QtGui.QPixmap(":/icons/images/list-music.png"))
            self.btn_playpause.setIcon(QIcon(QDir.current().filePath("ui/images/play.png")))
    
    def slider_enable(self):
        if not self.horizontalSlider.isEnabled():
            self.horizontalSlider.setEnabled(True)

    def format_time(self, seconds):
        time_delta = timedelta(seconds=seconds)
        hours, remainder = divmod(time_delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_time = "{:02}:{:02}".format(minutes, seconds)
        if time_delta.days > 0 or hours > 0:
            formatted_time = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)

        return formatted_time
    
    def time_label_counter(self):
        if self.is_playing == True:
            time_counter = self.horizontalSlider.value()
            self.remaining_time.setText(str(self.format_time(self.horizontalSlider.maximum() - time_counter)))
            self.elapsed_time.setText(str(self.format_time(time_counter)))


    def fill_list(self, open_file):
        
        for song in range(len(open_file)):
            this_song =self.tag_extractor(open_file[song])
            song_dict = {
                "path": this_song['Path'],
                "title": this_song["Title"],
                "album": this_song["Album"],
                "artist": this_song["Artist"],
                "file_name" : this_song["File_Name"],
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
        open_file = list(QFileDialog.getOpenFileNames(caption="Open Song", filter="MP3 files (*.mp3)")[0])
        if open_file != []:
            self.fill_list(open_file)
            self.slider_enable()
            self.table_column_size()
            if self.is_playing == False and self.pause == False:
                self.table_songs.selectRow(0)
                self.current_song = self.song_list[0]['path']
                self.play_pause()
            
    def next(self):   
        if len(self.song_list) >1 :
            self.initial_slider()
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
            self.set_slider_maximum()
            self.play_pause()
        
    def prev(self):
        if len(self.song_list) > 1 :
            self.initial_slider()
            for item in self.song_list:
                if item['path'] == self.current_song:
                    current_row = self.song_list.index(item)
                    break
            
            if current_row != 0: #back to the first row if on the last row
                self.current_song = self.song_list[current_row-1]['path']
                self.table_songs.selectRow(current_row-1)
            else:
                self.current_song = self.song_list[len(self.song_list)-1]['path']
                self.table_songs.selectRow(len(self.song_list)-1)           
            self.stop()
            self.set_slider_maximum()
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
        if len(self.song_list) > 0:
            current_row = self.table_songs.currentRow()
            seek_value = self.song_list[current_row]['duration']
            mixer.music.set_pos((self.horizontalSlider.value()))
            self.horizontalSlider.setValue(int((self.horizontalSlider.value())))

    def get_sec(self, time_str):
        """Get seconds from time."""
        m, s = time_str.split(':')
        return int(m) * 60 + int(s)

    def tag_extractor(self, mysong):
        audio = ID3(mysong)
        if audio.get("TPE1") is not None and audio.get("TPE1").text is not None and len(audio.get("TPE1").text) > 0:
            song_artist = audio.get("TPE1").text[0]
        else:
            song_artist = "Unknown Artist"
            
        song_artwork = audio.get("APIC:")
        
        if audio.get("TALB") is not None and audio.get("TALB").text is not None and len(audio.get("TALB").text) > 0:
            song_album = audio.get("TALB").text[0]
        else:
            song_album = "Unknown Album"

        song_path = mysong
        file_name_without_path = os.path.basename(mysong)
        song_file_name = os.path.splitext(file_name_without_path)[0]
        
        if audio.get("TIT2") is not None:
            song_name = audio.get("TALB").text[0]
        else:
            song_name = "Unknown Title"
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
            self.table_songs.selectRow(rnd)
            self.stop()
            self.set_slider_maximum()
            self.play_pause()

    def update_slider_position(self):
        self.slider_current_position = 0
        self.slider_current_position += self.horizontalSlider.value() + 1
        self.horizontalSlider.setValue(self.slider_current_position)
        self.time_label_counter()

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