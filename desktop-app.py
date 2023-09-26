
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
import requests
class FileUploader(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'File Uploader'

    def build(self):
        layout = BoxLayout(orientation='vertical')

        label = Label(text='Pilih file untuk diunggah:')
        layout.add_widget(label)

        file_chooser = FileChooserIconView()
        layout.add_widget(file_chooser)

        upload_button = Button(text='Unggah')
        upload_button.bind(on_release=lambda x: self.upload_file(file_chooser.path))
        layout.add_widget(upload_button)

        return layout

    def upload_file(self, file_path):
        url = ''
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            print('File berhasil diunggah')
        else:
            print('Gagal mengunggah file')

if __name__ == '__main__':
    FileUploader().run()