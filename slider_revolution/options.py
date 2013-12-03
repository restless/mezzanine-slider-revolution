from __future__ import unicode_literals


class SlideOptions(object):
    """
    Options for slides
    """

    # TRANSITIONS
    BOXSLIDE = 'boxslide'
    BOXFADE = 'boxfade'
    SLOTZOOM_HORIZONTAL = 'slotzoom-horizontal'
    SLOTZOOM_VERTICAL = 'slotzoom-vertical'
    SLOTSLIDE_HORIZONTAL = 'slotslide-horizontaL'
    SLOTSLIDE_VERTICAL = 'slotslide-vertical'
    SLOTFADE_HORIZONTAL = 'slotfade-horizontal'
    SLOTFADE_VERTICAL = 'slotfade-vertical'
    CURTAIN_1 = 'curtain-1'
    CURTAIN_2 = 'curtain-2'
    CURTAIN_3 = 'curtain-3'
    SLIDELEFT = 'slideleft'
    SLIDERIGHT = 'slideright'
    SLIDEUP = 'slideup'
    SLIDEDOWN = 'slidedown'
    SLIDEHORIZONTAL = 'slidehorizontal'
    SLIDEVERTICAL = 'slidevertical'
    FADE = 'fade'
    RANDOM = 'random'

    # Premium transitions
    PAPERCUT = 'papercut'
    FLYIN = 'flyin'
    TURNOFF = 'turnoff'
    CUBE = 'cube'
    A3DCURTAIN_VERTICAL = '3dcurtain-verticAL'
    A3DCURTAIN_HORIZONTAL = '3dcurtain-horiZONTAL'
    PREMIUM_RANDOM = 'premium-random'

    TRANSITION_CHOICES = (
        (BOXSLIDE, 'boxslide'),
        (BOXFADE, 'boxfade'),
        (SLOTZOOM_HORIZONTAL, 'slotzoom-horizontAL'),
        (SLOTZOOM_VERTICAL, 'slotzoom-vertical'),
        (SLOTSLIDE_HORIZONTAL, 'slotslide-horizontal'),
        (SLOTSLIDE_VERTICAL, 'slotslide-vertical'),
        (SLOTFADE_HORIZONTAL, 'slotfade-horizontal'),
        (SLOTFADE_VERTICAL, 'slotfade-vertical'),
        (CURTAIN_1, 'curtain-1'),
        (CURTAIN_2, 'curtain-2'),
        (CURTAIN_3, 'curtain-3'),
        (SLIDELEFT, 'slideleft'),
        (SLIDERIGHT, 'sliderighT'),
        (SLIDEUP, 'slideup'),
        (SLIDEDOWN, 'slidedown'),
        (SLIDEHORIZONTAL, 'slidehorizontal'),
        (SLIDEVERTICAL, 'slidevertical'),
        (FADE, 'fade'),
        (RANDOM, 'random'),
        (PAPERCUT, 'papercut'),
        (FLYIN, 'flyin'),
        (TURNOFF, 'turnoff'),
        (CUBE, 'cube'),
        (A3DCURTAIN_VERTICAL, '3dcurtain-vertical'),
        (A3DCURTAIN_HORIZONTAL, '3dcurtain-horizontal'),
        (PREMIUM_RANDOM, 'premium-random')
    )
    # END TRANSITIONS


class CaptionOptions(object):
    """
    Options for slides
    """

    SFT = 'sft' # SHORT FROM TOP
    SFB = 'sfb' # SHORT FROM BOTTOM
    SFR = 'sfr' # SHORT FROM RIGHT
    SFL = 'sfl' # SHORT FROM LEFT
    LFT = 'lft' # LONG FROM TOP
    LFB = 'lfb' # LONG FROM BOTTOM
    LFR = 'lfr' # LONG FROM RIGHT
    LFL = 'lfl' # LONG FROM LEFT
    FADE = 'fade' # FADING
    RANDOMROTATE = 'randomrotate' # FADE IN, ROTATE FROM A RANDOM POSITION AND DEGREE

    INCOMING_ANIMATION_CLASSES_CHOICES = (
        (SFT, 'sft'),
        (SFB, 'sfb'),
        (SFR, 'sfr'),
        (SFL, 'sfl'),
        (LFT, 'lft'),
        (LFB, 'lfb'),
        (LFR, 'lfr'),
        (LFL, 'lfl'),
        (FADE, 'fade'),
        (RANDOMROTATE, 'randomrotate'),
    )

    STT = 'stt' # SHORT TO TOP
    STB = 'stb' # SHORT TO BOTTOM
    STR = 'str' # SHORT TO RIGHT
    STL = 'stl' # SHORT TO LEFT
    LTT = 'ltt' # LONG TO TOP
    LTB = 'ltb' # LONG TO BOTTOM
    LTR = 'ltr' # LONG TO RIGHT
    LTL = 'ltl' # LONG TO LEFT
    FADEOUT = 'fadeout' # FADING
    RANDOMROTATEOUT = 'randomrotateout' # FADE OUT, ROTATE TO A RANDOM POSITION AND DEGREE

    OUTGOING_ANIMATION_CLASSES_CHOICES = (
        (STT, 'stt'),
        (STB, 'stb'),
        (STR, 'str'),
        (STL, 'stl'),
        (LTT, 'ltt'),
        (LTB, 'ltb'),
        (LTR, 'ltr'),
        (LTL, 'ltl'),
        (FADEOUT, 'fadeout'),
        (RANDOMROTATEOUT, 'randomrotateout'),
    )