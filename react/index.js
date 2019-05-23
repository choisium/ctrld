import React from 'react';
import ReactDOM from 'react-dom';

import TuiCalendar from './TuiCalendar';

var home = document.getElementById("home");

class Home extends React.Component {
  render() {
    return (
      <div>
        <p>Hello, World!</p>
        <TuiCalendar />
      </div>
    )
  }
}

// if (home) {
//   ReactDOM.render(
//     <Grid container alignItems='center' justify='center' style={{width: '100%'}}>
//       <MuiThemeProvider theme={hyosub_theme}>
//         <Home />
//       </MuiThemeProvider>
//     </Grid>
//   , home);
// }

if(home) {
  ReactDOM.render(
    <Home />
  , home);
}