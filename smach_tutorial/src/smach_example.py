#! /usr/bin/env python

import rospy
import smach
import smach_ros

# define smach state
# a state is a node incluing an execution program, and output the outcome of the current node
class Eat(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1', 'outcome2'])
        # super(Eat, self).__init__(self, outcomes=['outcome1', 'outcome2'])
        self.count = 0

    def execute(self, userdata):
        rospy.loginfo("Execute state Eat, count:{}".format(self.count))
        if self.count < 3:
            self.count += 1
            return 'outcome1'
        else:
            return 'outcome2'

# another state 
class Sleep(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome3'])
        
    def execute(self, userdata):
        rospy.loginfo("Execute state Sleep")
        return 'outcome3'

def main():
    rospy.init_node('smach_example')

    # create a smach state machine
    sm = smach.StateMachine(outcomes=['outcome4'])

    # open the container
    with sm:
        smach.StateMachine.add('Eat', Eat(),
        transitions={'outcome1':'Sleep', 'outcome2':'outcome4'})

        smach.StateMachine.add('Sleep', Sleep(),
        transitions={'outcome3':'Eat'})

    outcome = sm.execute()

if __name__ == '__main__':
    main()
