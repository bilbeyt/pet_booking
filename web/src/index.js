import React from 'react';
import ReactDOM from 'react-dom';
import {
  Router, Route, Switch,
} from 'react-router';
import History from './common/History';
import Routes from './Routes';
import Index from './components/Index';


ReactDOM.render(
  <React.StrictMode>
    <Router history={History}>
      <Switch>
        <Route path={Routes.dashboard} exact component={Index.Dashboard}/>
        <Route path={Routes.login} exact component={Index.Login}/>
        <Route path={Routes.register} exact component={Index.Register}/>
        <Route path={Routes.clinicAdd} exact component={Index.AddClinic}/>
        <Route path={Routes.veterinarianAdd} exact component={Index.AddVeterinarian}/>
        <Route path={Routes.petAdd} exact component={Index.AddPet}/>
        <Route path={Routes.appointmentCreate} exact component={Index.CreateAppointment}/>
        <Route path={Routes.appointmentSearch} exact component={Index.SearchAppointment}/>
      </Switch>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);
