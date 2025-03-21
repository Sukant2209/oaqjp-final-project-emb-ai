'''
This is a Test module for run unit test for emotion_
detector function
'''

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    '''Test Class for emotion_deetctor function'''

    def test_emotion(self):

        '''
        Running multiple testcase base on different text to get
        different dominant emotion
        '''

        res1 = emotion_detector("I am glad this happened")
        self.assertEqual(res1.get("dominant_emotion"),"joy")

        res2 = emotion_detector("I am really mad about this")
        self.assertEqual(res2.get("dominant_emotion"),"anger")

        res3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res3.get("dominant_emotion"),"disgust")

        res4 = emotion_detector("I am so sad about this")
        self.assertEqual(res4.get("dominant_emotion"),"sadness")

        res5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res5.get("dominant_emotion"),"fear")

unittest.main()
