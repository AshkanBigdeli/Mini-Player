if song_dict not in self.song_list:
            for i in range(len(open_file)):
                self.song_list.append(song_dict)
                row = self.table_songs.rowCount()
                self.table_songs.insertRow(row)
                self.table_songs.setItem(row, 0, QTableWidgetItem(self.song_list[i]['artist']))
                self.table_songs.setItem(row, 1, QTableWidgetItem(str(self.song_list[i]['title'])))
                self.table_songs.setItem(row, 2, QTableWidgetItem(self.song_list[i]['album']))
                self.table_songs.setItem(row, 3, QTableWidgetItem(str(self.song_list[i]['duration'])))
        else:
            pass