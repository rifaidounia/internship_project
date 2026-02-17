from selenium.webdriver.common.by import By
from pages.base_page.py import Page

class MainPage(Page):

   def open_main_page(self):
     self.open_url("/io")


