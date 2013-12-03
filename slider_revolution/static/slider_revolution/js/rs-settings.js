/* SLIDER_ID has to be set in the template */

var tpj=jQuery;
tpj.noConflict();
tpj(document).ready(function() {
  if (tpj.fn.cssOriginal!=undefined)
  tpj.fn.css = tpj.fn.cssOriginal;
  tpj(SLIDER_ID).revolution({
     delay:9000,
     startwidth:960,
     startheight:500,

     onHoverStop:"on",

     thumbWidth:100,
     thumbHeight:50,
     thumbAmount:3,

     hideThumbs:0,

     navigationType:"bullet",
     navigationArrows:"solo",
     navigationStyle:"round",
     navigationHAlign:"left",
     navigationVAlign:"bottom",
     navigationHOffset:30,
     navigationVOffset:30,

     soloArrowLeftHalign:"left",
     soloArrowLeftValign:"center",
     soloArrowLeftHOffset:20,
     soloArrowLeftVOffset:0,

     soloArrowRightHalign:"right",
     soloArrowRightValign:"center",
     soloArrowRightHOffset:20,
     soloArrowRightVOffset:0,

     touchenabled:"on",

     stopAtSlide:-1,
     stopAfterLoops:-1,
     hideCaptionAtLimit:0,
     hideAllCaptionAtLilmit:0,
     hideSliderAtLimit:0,

     fullWidth:"off",
     fullScreen:"off",
     fullScreenOffsetContainer:"#topheader-to-offset",

     shadow:0

  });

});