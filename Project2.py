"""
Project 2 - File Download with Threads and Multiprocesses
The project is to design a program that uses both processes and threads to download files from a list of URLs.
The program should be able to download multiple files
simultaneously using threads and/or processes to speed up the download process.

"""
import multiprocessing
import threading
import time
from threading import Thread ,current_thread
import requests

url = ["https://github.com/favicon.ico"]

def download_file (url,file):
    response = requests.get(url)
    open(file, "wb").write(response.content)
def download_files_thread(dir,list_url):
    s=time.perf_counter()

    for index ,url in enumerate(list_url):
        print(url)
        if str(url).endswith(".pdf"):
            thread=threading.Thread(target=download_file,args=(url,f"{dir}/sample{index}.pdf"))
        else:
            thread = threading.Thread(target=download_file, args=(url, f"{dir}/sample{index}.dat"))

        thread.start()
        thread.join()
        e = time.perf_counter()
        print(f"threding time {e - s}")
def download_files_process(dir,list_url):
    s=time.perf_counter()
    for index, url in enumerate(list_url):
        p = multiprocessing.Process(target=download_file, args=(url, f"{dir}/sample{index}.pdf"))
        p.start()
        p.join()
    e=time.perf_counter()
    print(f"proccess time{e-s}")
def download_files_parallel(dir,list_url):
    download_files_thread(dir,list_url)
    download_files_process(dir,list_url)
if __name__=="__main__":

    dir = "C:/Users/ADMIN\PycharmProjects/pythonProject/Week5/"
    list_url=["https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/sample.pdf",
    "http://ovh.net/files/10Gb.dat",
    "http://ovh.net/files/1Gb.dat"]
    download_files_parallel(dir,list_url)


# download_file(url, "github.ico")
