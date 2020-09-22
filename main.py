import os
import time
import threading
import youtube_dl



# I could've downloaded the repository and then edited the output files myself but I found it better to just
# write these loggers and options for each channel. If I downloaded the repository I would have to alter it each time they made
# an update and that's a bit too much work for what this is.

class AnatomyOfAFighterLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[Anatomy of a Fighter] ' + msg)
	def error(self,msg):
		print('[Anatomy of a Fighter]' + msg)

class BernardoFariaLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[Bernardo Faria] ' + msg)
	def error(self,msg):
		print('[Bernardo Faria]' + msg)
	
class BobRossLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[Bob Ross] ' + msg)
	def error(self,msg):
		print('[Bob Ross]' + msg)


class BoxingLegendsLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[BLTV] ' + msg)
	def error(self,msg):
		print('[BLTV]' + msg)

class ClothMapLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[Cloth Map] ' + msg)
	def error(self,msg):
		print('[Cloth Map]' + msg)

class FallOfCivilizationsLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[Fall of Civilizations] ' + msg)
	def error(self,msg):
		print('[Fall of Civilizations]' + msg)

class FireOfLearningLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[Fire of Learning] ' + msg)
	def error(self,msg):
		print('[Fire of Learning]' + msg)

class FloGrapplingLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[FloGrappling] ' + msg)
	def error(self,msg):
		print('[FloGrappling]' + msg)

class FreeDawkinsLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[FreeDawkins] ' + msg)
	def error(self,msg):
		print('[FreeDawkins]' + msg)

class HBOBoxingLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[HBO Boxing] ' + msg)
	def error(self,msg):
		print('[BO Boxing]' + msg)

class IAmTheBayLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[iAmTheBay] ' + msg)
	def error(self,msg):
		print('[iAmTheBay]' + msg)

class MetamorisLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[Metamoris] ' + msg)
	def error(self,msg):
		print('[Metamoris]' + msg)

class MixedMollyWhopperyLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[Mixed Molly Whoppery] ' + msg)
	def error(self,msg):
		print('[Mixed Molly Whoppery]' + msg)

class NoClipLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[No Clip] ' + msg)
	def error(self,msg):
		print('[No Clip]' + msg)

class ONEChampionshipLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[ONE Championship] ' + msg)
	def error(self,msg):
		print('[ONE Championship]' + msg)

class RunThroughTheTapeLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[Run Through the Tape] ' + msg)
	def error(self,msg):
		print('[Run Through the Tape]' + msg)

class UFCLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[UFC] ' + msg)
	def error(self,msg):
		print('[UFC]' + msg)

class UFCEspanolLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[UFC Espanol] ' + msg)
	def error(self,msg):
		print('[UFC Espanol]' + msg)

class VetRanchLogger():
	def debug(self,msg):
		pass
	def warning(self,msg):
		print('[Vet Ranch] ' + msg)
	def error(self,msg):
		print('[Vet Ranch]' + msg)

ydl_opts_anatomy_of_a_fighter ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':AnatomyOfAFighterLogger(),
	'outtmpl':"%(playlist_uploader)s/%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s",
}

ydl_opts_bernardo_faria ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':BernardoFariaLogger(),
	'outtmpl':'%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_bob_ross ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':BobRossLogger(),
	'outtmpl':'%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_boxing_legends_tv ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':BoxingLegendsLogger(),
	'outtmpl':'%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_cloth_map ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':ClothMapLogger(),
	'outtmpl':'%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_fall_of_civilizations ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':FallOfCivilizationsLogger(),
	'outtmpl':'%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_fire_of_learning ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':FireOfLearningLogger(),
	'outtmpl':'%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_flo_grappling ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':FloGrapplingLogger(),
	'outtmpl':'%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_free_dawkins ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':FreeDawkinsLogger(),
	'outtmpl':'%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_hbo_boxing ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':HBOBoxingLogger(),
	'outtmpl':'%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_i_am_the_bay ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':IAmTheBayLogger(),
	'outtmpl':'%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_metatmoris ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':MetamorisLogger(),
	'outtmpl':'%(playlist_uploader)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_mixed_molly_whoppery ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':MixedMollyWhopperyLogger(),
	'outtmpl':'%(playlist_uploader)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_no_clip ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':NoClipLogger(),
	'outtmpl':'%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_one_championship ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':ONEChampionshipLogger(),
	'outtmpl':'%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_run_through_the_tape ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':RunThroughTheTapeLogger(),
	'outtmpl':'/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_ufc ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'matchtitle':'Free Fight',
	'logger':UFCLogger(),
	'outtmpl':'%(uploader)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_ufc_espanol ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'matchtitle':'Pelea Gratis',
	'logger':UFCEspanolLogger(),
	'outtmpl':'%(uploader)s/%(title)s - %(upload_date)s.%(ext)s',
}

ydl_opts_vet_ranch ={
	'format':"(bestvideo[vcodec^=av01][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=1080][ext=mp4]/bestvideo[vcodec=vp9.2][height>=1080][ext=mp4]/bestvideo[vcodec=vp9][height>=1080][ext=mp4]/bestvideo[height>=1080][ext=mp4]/bestvideo[vcodec^=av01][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][fps>30][ext=mp4]/bestvideo[vcodec=vp9][height>=720][fps>30][ext=mp4]/bestvideo[vcodec^=av01][height>=720][ext=mp4]/bestvideo[vcodec=vp9.2][height>=720][ext=mp4]/bestvideo[vcodec=vp9][height>=720][ext=mp4]/bestvideo[height>=720][ext=mp4]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best",
	'ignoreerrors':True,
	'merge_output_format':'mkv',
	'download-archive':'archive.txt',
	'cookiefile':'cookies.txt',
	'geo_bypass':True,
	'logger':VetRanchLogger(),
	'outtmpl':'%(playlist_uploader)s/%(playlist)s/%(title)s - %(upload_date)s.%(ext)s',
}

# I had two different functions that I combined to 1
def download(channel_tag ,dl_opts, links, sleep_length):
	print (channel_tag + ' Starting next run...')
	with youtube_dl.YoutubeDL(dl_opts) as ydl:
		ydl.download(links)
	print(channel_tag + ' Waiting to start next run')
	time.sleep(sleep_length)

thread_list =[]

def start_threads():
	for t in thread_list:
		t.start()

def append_threads():
	# Anatomy of a Fighter
	thread_anatomy_of_a_fighter = threading.Thread(target=download,args=('[Anatomy of a Fighter]',ydl_opts_anatomy_of_a_fighter,['https://www.youtube.com/c/AnatomyofaFighter/playlists','https://www.youtube.com/c/AnatomyofaFighter/'],1200))
	thread_list.append(thread_anatomy_of_a_fighter)

	# Bernardo Faria
	thread_bernardo_faria = threading.Thread(target=download,args=('[Bernardo Faria]', ydl_opts_bernardo_faria,['https://www.youtube.com/c/BernardoFariaBJJ/playlists','https://www.youtube.com/c/BernardoFariaBJJ/'],1200 ))
	thread_list.append(thread_bernardo_faria)	

	# Bob Ross
	thread_bob_ross = threading.Thread(target=download,args=('[Bob Ross]',ydl_opts_bob_ross,['https://www.youtube.com/user/BobRossInc/playlists','https://www.youtube.com/user/BobRossInc'],1200))
	thread_list.append(thread_bob_ross)

	# Boxing Legends TV
	thread_boxing_legends = threading.Thread(target=download,args=('[Boxing Legends]',ydl_opts_boxing_legends_tv,['https://www.youtube.com/c/BoxingLegendsTV/playlists','https://www.youtube.com/c/BoxingLegendsTV/','https://www.youtube.com/c/FighterWarriorTV'],1200))
	thread_list.append(thread_boxing_legends)

	# Cloth Map
	thread_cloth_map = threading.Thread(target=download,args=('[Cloth Map]',ydl_opts_cloth_map,['https://www.youtube.com/c/clothmap/playlists','https://www.youtube.com/c/clothmap/'],1200))
	thread_list.append(thread_cloth_map)

	# Fall of Civilizations
	thread_fall_of_civilizations = threading.Thread(target=download,args=('[Fall of Civilizations]',ydl_opts_fall_of_civilizations,['https://www.youtube.com/c/FallofCivilizationsPodcast/playlists','https://www.youtube.com/c/FallofCivilizationsPodcast/'],1200)) 
	thread_list.append(thread_fall_of_civilizations)

	# Fire of Learning
	thread_fire_of_learning = threading.Thread(target=download,args=('[Fire of Learning]',ydl_opts_fire_of_learning,['https://www.youtube.com/user/Fireoflearning/playlists','https://www.youtube.com/user/Fireoflearning'],1200))
	thread_list.append(thread_fire_of_learning)

	# FloGrappling
	thread_flo_grappling = threading.Thread(target=download,args=('[FloGrappling]',ydl_opts_flo_grappling,['https://www.youtube.com/c/flograppling/playlists','https://www.youtube.com/c/flograppling'],1200))
	thread_list.append(thread_flo_grappling)

	# Free Dawkins
	thread_free_dawkins = threading.Thread(target=download,args=('[Free Dawkins]',ydl_opts_free_dawkins, ['https://www.youtube.com/channel/UCEjOSbbaOfgnfRODEEMYlCw/playlists','https://www.youtube.com/channel/UCu3_PoMtnYClsRFpS_cUAmg/playlists','https://www.youtube.com/channel/UC4xB9I9vmsIg3Les2OFK0dA/playlists','https://www.youtube.com/channel/UCULluQyJiylEgjwDYNkHAuw/playlists','https://www.youtube.com/channel/UCEjOSbbaOfgnfRODEEMYlCw','https://www.youtube.com/channel/UCu3_PoMtnYClsRFpS_cUAmg','https://www.youtube.com/channel/UC4xB9I9vmsIg3Les2OFK0dA','https://www.youtube.com/channel/UCULluQyJiylEgjwDYNkHAuw'],1200))
	thread_list.append(thread_free_dawkins)

	# HBO Boxing
	thread_hbo_boxing = threading.Thread(target=download,args=('[HBO Boxing]', ydl_opts_hbo_boxing,['https://www.youtube.com/user/HBOsports/playlists','https://www.youtube.com/user/HBOsports'],1200))
	thread_list.append(thread_hbo_boxing)

	# iAmTheBay
	thread_i_am_the_bay = threading.Thread(target=download,args=('[iAmTheBay]',ydl_opts_i_am_the_bay,['https://www.youtube.com/c/iAmTheBay'],1200))
	thread_list.append(thread_i_am_the_bay)

	# Metamoris
	thread_metamoris = threading.Thread(target=download,args=('[Metamoris]',ydl_opts_metatmoris,['https://www.youtube.com/playlist?list=PLO_8vIgRfQ3JBG0eqm7cXJqvN11ijucQ6'],1200))
	thread_list.append(thread_metamoris)

	# Mixed Molly Whoppery
	thread_mixed_molly_whoppery = threading.Thread(target=download,args=('[Mixed Molly Whoppery]',ydl_opts_mixed_molly_whoppery,['https://www.youtube.com/c/MollyWhopMMA/'],1200))
	thread_list.append(thread_mixed_molly_whoppery)

	# NoClip
	thread_no_clip = threading.Thread(target=download,args=('[NoClip]',ydl_opts_no_clip,['https://www.youtube.com/c/NoclipVideo/playlists','https://www.youtube.com/c/NoclipVideo'],1200))
	thread_list.append(thread_no_clip)

	# ONE Championship (Bleacher Report Live)
	thread_one_championship = threading.Thread(target=download,args=('[ONE Championship]',ydl_opts_one_championship,['https://www.youtube.com/playlist?list=PLMezQWSbBUI15UtGze-06zfaapOxYDPXj'],1200))
	thread_list.append(thread_one_championship)

	# Run Through the Tape
	thread_run_through_the_tape = threading.Thread(target=download,args=('[Run Through the Tape]',ydl_opts_run_through_the_tape,['https://www.youtube.com/channel/UCmHw6G_DLFGcfa4aXOmb4bw/playlists','https://www.youtube.com/channel/UC8e9Z_lx4xs0mrZlxcN8hAQ/playlists','https://www.youtube.com/channel/UCUUpXhSbaBexwibfW0g9Jhw/playlists','https://www.youtube.com/channel/UCmHw6G_DLFGcfa4aXOmb4bw','https://www.youtube.com/channel/UC8e9Z_lx4xs0mrZlxcN8hAQ','https://www.youtube.com/channel/UCUUpXhSbaBexwibfW0g9Jhw'],1200))
	thread_list.append(thread_run_through_the_tape)

	# UFC
	thread_ufc = threading.Thread(target=download,args=('[UFC]',ydl_opts_ufc,['https://www.youtube.com/c/UFC'],1200))
	thread_list.append(thread_ufc)

	# UFC Espanol
	thread_ufc_espanol = threading.Thread(target=download,args=('[UFC Espanol]',ydl_opts_ufc_espanol,['https://www.youtube.com/c/ufcespanol/'],1200))
	thread_list.append(thread_ufc_espanol)

	# Vet Ranch
	thread_vet_ranch = threading.Thread(target=download,args=('[Vet Ranch]',ydl_opts_vet_ranch,['https://www.youtube.com/user/VetRanch/playlists','https://www.youtube.com/user/VetRanch'],1200))
	thread_list.append(thread_vet_ranch)
	
	
	


def main():
	append_threads()
	start_threads()

if __name__ == "__main__":
    main()
    	
