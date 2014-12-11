import unittest
from selenium import webdriver
import subprocess
import wsgi
import os
import httplib
import dircache
import socket

class DisplayPage(unittest.TestCase):

	host = 'localhost'
	host_url = 'http://localhost:8888'
	port_number = 8888
	htdoc_directory = './htdocs/'
	static_directory = './static/'

	@classmethod
	def setUpClass(self):
		print("In setUp()")
		args = ['python','/users/edwin/PycharmProjects/funwithwsgi/funwithwsgi/wsgi-server.py']
		self.subProc = subprocess.Popen(args)
		self.browser = webdriver.Firefox()
		result = self.browser.get(self.host_url)
		print result

	def testOfTests(self):
		#page = httplib.HTTPConnection('localhost', 8888, None, )
		page = httplib.HTTPConnection(self.host,  port = 8888, strict = None ,timeout = socket._GLOBAL_DEFAULT_TIMEOUT)
		page.request("HEAD", '')
		self.assertEqual(page.getresponse().status, 200)

	def testTitle(self):
		self.assertIn('Hello World', self.browser.title)

	def testCheckIfDirectoriesExist(self):
		listDirs = [self.htdoc_directory, self.static_directory]
		for directories in listDirs:
			self.assertTrue(os.path.exists(directories))

	def testFileNamesAreUrllinks(self):
		currentUrl = self.browser.current_url 
		htDocsFiles = self.fetchFilesFromDirectory(self.htdoc_directory)
		for htDocFile in htDocsFiles:
			page = httplib.HTTPConnection(self.host, self.port_number, strict = None, timeout = socket._GLOBAL_DEFAULT_TIMEOUT)

			page.request("HEAD", str(htDocFile[:-5]))
			self.assertEqual(page.getresponse().status, 200)

	def fetchFilesFromDirectory(self, directory):
		directory_listing = dircache.listdir(self.htdoc_directory)
		return directory_listing

	@classmethod
	def tearDownClass(self):
		print("In tearDown()")
		self.browser.quit()
		self.subProc.kill()

if __name__ == '__main__':
	unittest.main()
