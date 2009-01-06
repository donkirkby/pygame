# This file is generated with mmp2sconscript
from scons_symbian import *

Import("*")

target     = TARGET_NAME
targettype = "dll"


includes    = [ 'deps/SDL/src', 'deps/SDL/src/video', 
                'deps/SDL/src/events', 'deps/SDL/src/audio', 
                'deps/SDL/src/audio/symbian', 'deps/SDL/src/main/symbian', 
                'deps/SDL/src/video/symbian', 'deps/SDL/src/thread', 
                'deps/SDL/src/thread/generic', 'deps/SDL/src/thread/symbian', 
                'deps/SDL/src/timer', 'deps/SDL/src/joystick', 
                'deps/SDL/symbian/inc', 'deps/SDL/inc/internal']

sysincludes = ['deps/SDL/include', '/epoc32/include', 
               'inc', '/epoc32/include/SDL', 
               '/epoc32/include/gles', 
               '/epoc32/include/EGL', 
               '/epoc32/include/libc', 
               ]

libraries  = ['euser',
 'fbscli',
 'ws32',
 'gdi',
 'mediaclientaudiostream',
 'avkon',
 'efsrv',
 'bafl',
 'apparc',
 'eikcore',
 'cone',
 'bitgdi',
 'scdv',
 'hal',
# 'libc',
# 'libm',
 'estlib']

# Static libraries
staticlibs = [ 'vorbis.lib', 'ogg.lib', 
             'SDL_ttf.lib', 
             'libsft2.lib',
             'pygame_libjpeg'
             ]
defines = []
sources = ['deps/SDL/symbian/src/vectorbuffer.cpp',
 'deps/SDL/symbian/src/sdlappsrv.cpp',
 'deps/SDL/symbian/src/sdlenv.cpp',
 'deps/SDL/symbian/src/dsa.cpp',
 'deps/SDL/symbian/src/streamplayer.cpp',
 'deps/SDL/symbian/src/sdlenvutils.cpp',
 'deps/SDL/src/SDL.c',
 'deps/SDL/src/SDL_error.c',
 'deps/SDL/src/SDL_fatal.c',
 'deps/SDL/src/main/symbian/SDL_libutils.cpp',
 'deps/SDL/src/main/symbian/SDL_main.cpp',
 'deps/SDL/src/cpuinfo/SDL_cpuinfo.c',
 'deps/SDL/src/video/SDL_blit.c',
 'deps/SDL/src/video/SDL_blit_0.c',
 'deps/SDL/src/video/SDL_blit_1.c',
 'deps/SDL/src/video/SDL_blit_A.c',
 'deps/SDL/src/video/SDL_blit_N.c',
 'deps/SDL/src/video/SDL_bmp.c',
 'deps/SDL/src/video/SDL_cursor.c',
 'deps/SDL/src/video/SDL_gamma.c',
 'deps/SDL/src/video/SDL_pixels.c',
 'deps/SDL/src/video/SDL_RLEaccel.c',
 'deps/SDL/src/video/SDL_stretch.c',
 'deps/SDL/src/video/SDL_surface.c',
 'deps/SDL/src/video/SDL_video.c',
 'deps/SDL/src/video/SDL_yuv.c',
 'deps/SDL/src/video/SDL_yuv_mmx.c',
 'deps/SDL/src/video/SDL_yuv_sw.c',
 'deps/SDL/src/video/symbian/SDL_epocvideo.cpp',
 'deps/SDL/src/video/symbian/SDL_epocevents.cpp',
 'deps/SDL/src/audio/SDL_audio.c',
 'deps/SDL/src/audio/SDL_audiocvt.c',
 'deps/SDL/src/audio/SDL_audiodev.c',
 'deps/SDL/src/audio/SDL_mixer.c',
 'deps/SDL/src/audio/SDL_wave.c',
 'deps/SDL/src/audio/symbian/SDL_epocaudio.cpp',
 'deps/SDL/src/thread/SDL_thread.c',
 'deps/SDL/src/thread/generic/SDL_syscond.c',
 'deps/SDL/src/thread/symbian/SDL_sysmutex.cpp',
 'deps/SDL/src/thread/symbian/SDL_syssem.cpp',
 'deps/SDL/src/thread/symbian/SDL_systhread.cpp',
 'deps/SDL/src/events/SDL_active.c',
 'deps/SDL/src/events/SDL_events.c',
 'deps/SDL/src/events/SDL_keyboard.c',
 'deps/SDL/src/events/SDL_mouse.c',
 'deps/SDL/src/events/SDL_quit.c',
 'deps/SDL/src/events/SDL_resize.c',
 'deps/SDL/src/timer/SDL_timer.c',
 'deps/SDL/src/timer/symbian/SDL_systimer.cpp',
 'deps/SDL/src/file/SDL_rwops.c',
 'deps/SDL/src/stdlib/SDL_string.c',
 'deps/SDL/src/stdlib/SDL_getenv.c']

 # Configure SDL_Mixer
sources += [
 'deps/SDL_mixer/mixer.c',
 'deps/SDL_mixer/music.c',
 #'deps/SDL_mixer/playwave.c',
 'deps/SDL_mixer/wavestream.c',
 'deps/SDL_mixer/effects_internal.c',
 'deps/SDL_mixer/effect_position.c',
 'deps/SDL_mixer/effect_stereoreverse.c',
 'deps/SDL_mixer/load_aiff.c',
 'deps/SDL_mixer/load_voc.c',
 'deps/SDL_mixer/load_ogg.c',
 'deps/SDL_mixer/dynamic_ogg.c',
 'deps/SDL_mixer/music_ogg.c',
]
sysincludes += ['deps/vorbis/include', 
               'deps/vorbis/include/vorbis', 
               'deps/ogg/include', 
               'deps/ogg/include/ogg']

defines += [ 'WAV_MUSIC', 'OGG_MUSIC', ]

# Configure SDL_ttf
sources += [
 'deps/SDL_ttf/SDL_ttf.c',
]

# Configure SDL_image
sources += Glob('deps/SDL_image/IMG*.c',)
defines += [
            'LOAD_JPG',
            'LOAD_BMP',
            'LOAD_GIF',
            'LOAD_TGA'
            #'LOAD_PNG' # requires glib. We need OpenC
            ]
sysincludes += [
    'deps/jpeg/', 
]



defines     +=['SYMBIANC', 'SYMBIAN_SERIES60', 
               'NO_SIGNAL_H', 'ENABLE_EPOC', 
               'DISABLE_JOYSTICK', 'DISABLE_CDROM',                
               ]

includes += ["deps/SDL_ttf/", "deps/sft2/inc/sys"]

SymbianProgram( target, targettype,
    sources = sources,
    includes    = includes,
    sysincludes = sysincludes,
    libraries   = staticlibs + libraries,
    defines     = defines,
    capabilities = CAPABILITIES,
    uid3 = UID3,
    package = PACKAGE_NAME,
)