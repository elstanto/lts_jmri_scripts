import jmri
from java.awt import Toolkit, Dimension
screensize = Toolkit.getDefaultToolkit().getScreenSize()

for frame in jmri.util.JmriJFrame.getFrameList():
    if frame.title == "Analogue Clock" and frame.isVisible():
        # Maximise frame
        frame.setExtendedState(frame.getExtendedState() | frame.MAXIMIZED_BOTH)
        # Now rescale inner panel and call scaleFace which uses this value to redraw the clock
        frame.getContentPane().getComponents()[0].setSize(Dimension(screensize.width, screensize.height-20))
        frame.getContentPane().getComponents()[0].scaleFace()
