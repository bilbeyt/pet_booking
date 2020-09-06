import React from 'react'
import Routes from '../Routes';
import axios from 'axios';


export default class Header extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            user: null
        }
    }

    componentDidMount(){
        const { history } = this.props;
        const refreshToken = localStorage.getItem("refresh");
        if (!refreshToken){
            history.push(Routes.login);
        }
        axios.post('http://localhost:8000/api/refresh/', null, {
            headers: { 'Authorization': `Bearer ${refreshToken}` }
        }).then(res => {
            localStorage.setItem("access", res.json());
        })
    }

    render(){
        return (
            <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
                <a class="navbar-brand" href="https://getbootstrap.com/docs/4.5/examples/navbar-static/#">Top navbar</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarCollapse">
                    <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                        <a class="nav-link" href="https://getbootstrap.com/docs/4.5/examples/navbar-static/#">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://getbootstrap.com/docs/4.5/examples/navbar-static/#">Link</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled" href="https://getbootstrap.com/docs/4.5/examples/navbar-static/#" tabindex="-1" aria-disabled="true">Disabled</a>
                    </li>
                    </ul>
                    <form class="form-inline mt-2 mt-md-0">
                        <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search"/>
                        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                    </form>
                </div>
            </nav>
        )
    }
}