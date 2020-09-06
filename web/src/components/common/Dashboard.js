import React from 'react';
import {Form, Button, Col } from 'react-bootstrap';
import Routes from '../../Routes';
import axios from 'axios';


export default class Dashboard extends React.Component{
    constructor(props){
        super(props);
    }

    login(){
        const {props} = this;
        const { state } = this;
        axios.post('http://localhost:8000/api/token/', { username: state.username, password: state.password })
        .then(res => {
            localStorage.setItem("access", res.data.access);
            localStorage.setItem("refresh", res.data.refresh);
            props.history.push(Routes.Dashboard);
        })
        .catch(() => alert("Wrong Credentials"))
    }

    render(){
        return (
            <Col md={{span:4, offset: 4}} id="loginPanel">
                <Form>
                    <Form.Group>
                        <Form.Label>Username</Form.Label>
                        <Form.Control
                            type="text"
                            onChange={(e) => {this.setState({username: e.currentTarget.value})}}
                        />
                    </Form.Group>
                    <Form.Group>
                        <Form.Label>Password</Form.Label>
                        <Form.Control
                            type="password"
                            onChange={(e) => {this.setState({password: e.currentTarget.value})}}
                        />
                    </Form.Group>
                    <Button onClick={() => {this.login()}}>Login</Button>
                </Form>
                <a href={Routes.register}>Register</a>
            </Col>
        )
    }
} 