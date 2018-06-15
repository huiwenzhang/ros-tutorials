#ifndef RQT_CONTROL_BASE_H
#define RQT_CONTROL_BASH_H

// headers
#include <ros/ros.h>
#include <ros/console.h>
// base class for plugin, if base class does not exist, create a new one
#include <rviz/panel.h>     

class QLineEdit;
namespace rqt_control_base
{
    class ControlBase: public rviz::Panel
    {
    Q_OBJECT
    public:
        ControlBase(QWidget* parent = 0);

        virtual void load(const rviz::Config& config);
        virtual void save(rviz::Config config) const;

    public Q_SLOTS:
        void setTopic(const QString& topic);

    // inner slots -- qt
    protected Q_SLOTS:
        void sendVel();     // publish velocity
        void updateLinearVel();     // update linear velociy accoridng to use's input
        void updateAngularVel();
        void updateTopic();

    protected:
        // topic
        QLineEdit* topic_editor_;
        QString topic_;

        // linear vel
        QLineEdit* topic_editor_1;
        QString topic_1;

        // angular vel
        QLineEdit* topic_editor_2;
        QString topic_2;


        // ros variables
        ros::Publisher velocity_pub_;
        ros::NodeHandle nh_;

        float linear_vel_;
        float angular_vel_;
    };
}
#endif