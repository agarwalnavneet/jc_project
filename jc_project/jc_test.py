import unittest

from my_jc import ActionProcessor

class JCTest(unittest.TestCase):
 
# Negative Tests
    def test_neg_1(self):
        data = '{"abc":"run", "time": 10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_2(self):
        data = '{"action":"run"}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_3(self):
        data = '{"time":"run"}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_4(self):
        data = '{"action":"", "time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_5(self):
        data = '{"":"run", "time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_6(self):
        data = '{"action":"run", "":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_7(self):
        data = '{"action":"run", time:10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_8(self):
        data = '{"action":run, "time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_9(self):
        data = '{"action":"run", "time":"10"}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_10(self):
        data = '{"action":"run                         ", "time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_11(self):
        data = '{"action":"run", "time":12345678901}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_12(self):
        data = '{"action                              ":"run", "time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_13(self):
        data = '{"action":"run", "                                time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_14(self):
        data = '{"action":10, "time":"run"}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_15(self):
        data = '{"time":10, "action":"run"}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_16(self):
        data = '{"Action":"run", "time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_17(self):
        data = '{"action":"run", "Time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_18(self):
        data = '{"action":"run", "":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_19(self):
        data = '{"action":"run", "ime":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_20(self):
        data = '{"action":"run", "time":10s}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_21(self):
        data = '{"action":"run" "time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_22(self):
        data = '{"action":"run". "time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_23(self):
        data = '{"action";"run", "time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_24(self):
        data = '{"action":"run", "time";10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_25(self):
        data = '["action":"run", "time":10]'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_26(self):
        data = '{"action":"run", "time":10]'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_27(self):
        data = '{{"action":"run", "time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_28(self):
        data = '{"action":"run, "time":10}}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_29(self):
        data = '"{action":"run", "time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_30(self):
        data = '{"action":"run", "time:"10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_31(self):
        data = '{"action:run", "time":10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')
        
    def test_neg_32(self):
        data = '{action:run, time:10}'
        s = ActionProcessor()
        res = s.addAction(data)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '')

# Functionality Tests        
    def test_action_1(self):
        s = ActionProcessor()
        stats = s.getStats()
        self.assertEqual(stats, '')        

    def test_action_2(self):
        d1 = '{"action":"run", "time":0}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":0}\n]\n')        

    def test_action_3(self):
        d1 = '{"action":"run", "time":10}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":10}\n]\n')        
        
    def test_action_4(self):
        d1 = '{"action":"run", "time":0}'
        d2 = '{"action":"run", "time":1.0}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":1.0}\n]\n')        

    def test_action_5(self):
        d1 = '{"action":"run", "time":0}'
        d2 = '{"action":"run", "time":10}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":10}\n]\n')        

    def test_action_6(self):
        d1 = '{"action":"run", "time":0}'
        d2 = '{"action":"run", "time":0}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":0}\n]\n')        

    def test_action_7(self):
        d1 = '{"action":"run", "time":10}'
        d2 = '{"action":"run", "time":1}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":5.5}\n]\n')        

    def test_action_8(self):
        d1 = '{"action":"run", "time":10}'
        d2 = '{"action":"jog", "time":1}'
        d3 = '{"action":"run", "time":1.0}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        res = s.addAction(d3)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":5.5},\n\t{"action":"jog", "avg":1}\n]\n')        

    def test_action_9(self):
        d1 = '{"action":"run", "time":10}'
        d2 = '{"action":"jog", "time":1}'
        d3 = '{"action":"run", "time":1.0}'
        d4 = '{"action":"jog", "time":399}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        res = s.addAction(d3)
        self.assertEqual(res, 0)
        res = s.addAction(d4)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":5.5},\n\t{"action":"jog", "avg":200}\n]\n')        

    def test_action_10(self):
        d1 = '{"action":"run", "time":10}'
        d2 = '{"action":"jog", "time":1}'
        d3 = '{"action":"jump", "time":1.0}'
        d4 = '{"action":"swim", "time":399}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        res = s.addAction(d3)
        self.assertEqual(res, 0)
        res = s.addAction(d4)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":10},\n\t{"action":"jog", "avg":1},\n\t{"action":"jump", "avg":1.0},\n\t{"action":"swim", "avg":399}\n]\n')        

    def test_action_11(self):
        d1 = '{"action":"run", "time":10}'
        d2 = '{"action":"jog", "time":1}'
        d3 = '{"action":"jump", "time":1.0}'
        d4 = '{"action":"swim", "time":399}'
        d5 = '{"action":"run", "time":50}'
        d6 = '{"action":"walk", "time":1}'
        d7 = '{"action":"jump", "time":100.0}'
        d8 = '{"action":"run", "time":200}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        res = s.addAction(d3)
        self.assertEqual(res, 0)
        res = s.addAction(d4)
        self.assertEqual(res, 0)
        res = s.addAction(d5)
        self.assertEqual(res, 0)
        res = s.addAction(d6)
        self.assertEqual(res, 0)
        res = s.addAction(d7)
        self.assertEqual(res, 0)
        res = s.addAction(d8)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":86.67},\n\t{"action":"jog", "avg":1},\n\t{"action":"jump", "avg":50.5},\n\t{"action":"swim", "avg":399},\n\t{"action":"walk", "avg":1}\n]\n')        

# Mix of functionality and negative tests
    def test_mix_1(self):
        d1 = '{"action":"run", "time":10}'
        d2 = '{"action":"run", "time":1}'
        d3 = '{"action:"run", "time":1}'
        s = ActionProcessor()
        res = s.addAction(d3)
        self.assertEqual(res, -1)
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":5.5}\n]\n')        

    def test_mix_2(self):
        d1 = '{"action":"run", "time":10}'
        d2 = '{"action":"run", "time":1}'
        d3 = '{"action:"run", "time":1}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d3)
        self.assertEqual(res, -1)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":5.5}\n]\n')        

    def test_mix_3(self):
        d1 = '{"action":"run", "time":10}'
        d2 = '{"action":"run", "time":1}'
        d3 = '{"action:"run", "time":1}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        res = s.addAction(d3)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":5.5}\n]\n')        

    def test_mix_4(self):
        d1 = '{"action":"run", "time":10}'
        d2 = '{"action":"jog", "time":1}'
        d3 = '{"action":"jump", "time":1.0}'
        d4 = '{"action":"swim", "time":399}'
        d5 = '{"action":"run", "time":50}'
        d6 = '{"action":"walk", "time":1}'
        d7 = '{"action":"jump", "time":100.0}'
        d8 = '{"action":"run", "time":200}'
        d9 = '{"action:"run", "time":1}'
        s = ActionProcessor()
        res = s.addAction(d9)
        self.assertEqual(res, -1)
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        res = s.addAction(d3)
        self.assertEqual(res, 0)
        res = s.addAction(d4)
        self.assertEqual(res, 0)
        res = s.addAction(d5)
        self.assertEqual(res, 0)
        res = s.addAction(d6)
        self.assertEqual(res, 0)
        res = s.addAction(d7)
        self.assertEqual(res, 0)
        res = s.addAction(d8)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":86.67},\n\t{"action":"jog", "avg":1},\n\t{"action":"jump", "avg":50.5},\n\t{"action":"swim", "avg":399},\n\t{"action":"walk", "avg":1}\n]\n')        

    def test_mix_5(self):
        d1 = '{"action":"run", "time":10}'
        d2 = '{"action":"jog", "time":1}'
        d3 = '{"action":"jump", "time":1.0}'
        d4 = '{"action":"swim", "time":399}'
        d5 = '{"action":"run", "time":50}'
        d6 = '{"action":"walk", "time":1}'
        d7 = '{"action":"jump", "time":100.0}'
        d8 = '{"action":"run", "time":200}'
        d9 = '{"action:"run", "time":1}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        res = s.addAction(d3)
        self.assertEqual(res, 0)
        res = s.addAction(d4)
        self.assertEqual(res, 0)
        res = s.addAction(d9)
        self.assertEqual(res, -1)
        res = s.addAction(d5)
        self.assertEqual(res, 0)
        res = s.addAction(d6)
        self.assertEqual(res, 0)
        res = s.addAction(d7)
        self.assertEqual(res, 0)
        res = s.addAction(d8)
        self.assertEqual(res, 0)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":86.67},\n\t{"action":"jog", "avg":1},\n\t{"action":"jump", "avg":50.5},\n\t{"action":"swim", "avg":399},\n\t{"action":"walk", "avg":1}\n]\n')        

    def test_mix_6(self):
        d1 = '{"action":"run", "time":10}'
        d2 = '{"action":"jog", "time":1}'
        d3 = '{"action":"jump", "time":1.0}'
        d4 = '{"action":"swim", "time":399}'
        d5 = '{"action":"run", "time":50}'
        d6 = '{"action":"walk", "time":1}'
        d7 = '{"action":"jump", "time":100.0}'
        d8 = '{"action":"run", "time":200}'
        d9 = '{"action:"run", "time":1}'
        s = ActionProcessor()
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        res = s.addAction(d3)
        self.assertEqual(res, 0)
        res = s.addAction(d4)
        self.assertEqual(res, 0)
        res = s.addAction(d5)
        self.assertEqual(res, 0)
        res = s.addAction(d6)
        self.assertEqual(res, 0)
        res = s.addAction(d7)
        self.assertEqual(res, 0)
        res = s.addAction(d8)
        self.assertEqual(res, 0)
        res = s.addAction(d9)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":86.67},\n\t{"action":"jog", "avg":1},\n\t{"action":"jump", "avg":50.5},\n\t{"action":"swim", "avg":399},\n\t{"action":"walk", "avg":1}\n]\n')        

    def test_mix_7(self):
        d1 = '{"action":"run", "time":10}'
        d2 = '{"action":"jog", "time":1}'
        d3 = '{"action":"jump", "time":1.0}'
        d4 = '{"action":"swim", "time":399}'
        d5 = '{"action":"run", "time":50}'
        d6 = '{"action":"walk", "time":1}'
        d7 = '{"action":"jump", "time":100.0}'
        d8 = '{"action":"run", "time":200}'
        d9 = '{"action:"run", "time":1}'
        s = ActionProcessor()
        res = s.addAction(d9)
        self.assertEqual(res, -1)
        res = s.addAction(d1)
        self.assertEqual(res, 0)
        res = s.addAction(d2)
        self.assertEqual(res, 0)
        res = s.addAction(d3)
        self.assertEqual(res, 0)
        res = s.addAction(d4)
        self.assertEqual(res, 0)
        res = s.addAction(d9)
        self.assertEqual(res, -1)
        res = s.addAction(d5)
        self.assertEqual(res, 0)
        res = s.addAction(d6)
        self.assertEqual(res, 0)
        res = s.addAction(d7)
        self.assertEqual(res, 0)
        res = s.addAction(d8)
        self.assertEqual(res, 0)
        res = s.addAction(d9)
        self.assertEqual(res, -1)
        stats = s.getStats()
        self.assertEqual(stats, '[\n\t{"action":"run", "avg":86.67},\n\t{"action":"jog", "avg":1},\n\t{"action":"jump", "avg":50.5},\n\t{"action":"swim", "avg":399},\n\t{"action":"walk", "avg":1}\n]\n')        

if __name__ == '__main__':
    unittest.main()
    
