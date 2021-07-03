import time
from voice_engine.kws import KWS
from voice_engine.source import Source

src = Source()
kws = KWS()
src.link(kws)

def on_detected(keyword):
    print('found {}'.format(keyword))
kws.on_detected = on_detected

kws.start()
src.start()
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break
kws.stop()
src.stop()
