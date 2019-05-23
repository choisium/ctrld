import React from "react";
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import classNames from 'classnames';
import compose from 'recompose/compose';
import withWidth from '@material-ui/core/withWidth';

import 'tui-calendar/dist/tui-calendar.css';
import Calendar from '@toast-ui/react-calendar';

const styles = theme => ({
});
  
class TuiCalendar extends React.Component {
  constructor(props){
    super(props);

    this.state = {
      today: new Date(),
    };

  }

  calendarRef = React.createRef();
  
  handleClickNextButton = () => {
    const calendarInstance = this.calendarRef.current.getInstance();

    calendarInstance.next();
  };

  render() {
    const { classes, width } = this.props;
    const { today } = this.state;

    return (
      <div style={{height: "800px"}}>
        <Calendar
          ref={this.calendarRef}
          calendars={[
            {
              id: '0',
              name: 'Private',
              bgColor: '#9e5fff',
              borderColor: '#9e5fff'
            },
            {
              id: '1',
              name: 'Company',
              bgColor: '#00a9ff',
              borderColor: '#00a9ff'
            }
          ]}
          view="month"
          defaultView="month"
          disableDblClick={false}
          height="90%"
          isReadOnly={false}
          month={{
            startDayOfWeek: 0,
            daynames: ['일', '월', '화', '수', '목', '금', '토']
          }}
          schedules={[
          ]}
          scheduleView={true}
          taskView={false}
          template={{
            milestone(schedule) {
              return `<span style="color:#fff;background-color: ${schedule.bgColor};">${
                schedule.title
              }</span>`;
            },
            milestoneTitle() {
              return '학교 일정';
            },
            allday(schedule) {
              return `${schedule.title}<i class="fa fa-refresh"></i>`;
            },
            alldayTitle() {
              return '학교 일정';
            }
          }}
          timezones={[
            {
              timezoneOffset: 540,
              displayLabel: 'GMT+09:00',
              tooltip: 'Seoul'
            }
          ]}
          useDetailPopup={true}
          useCreationPopup={true}
          week={{
            showTimezoneCollapseButton: true,
            timezonesCollapsed: true
          }}
        />
        <button onClick={this.handleClickNextButton}>Go next!</button>
      </div>
    );
  }
}

TuiCalendar.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default compose(withStyles(styles, {withTheme: true}), withWidth())(TuiCalendar);
