import React from 'react';
import {Form, Button, Col } from 'react-bootstrap';
import Routes from '../../Routes';
import axios from 'axios';


export default class Register extends React.Component{

    componentDidMount(){
        const {props} = this;
        axios.get('http://localhost:8000/api/groups/')
        .then(res => {
            this.setState({
                groups: res.json()
            })
        })
        .catch(err => alert("Wrong Credentials"))
    }

    register(){
        const {props} = this;
        const { state } = this;
        axios.post('http://localhost:8000/api/users/create/', state)
        .then(res => {
            localStorage.setItem("access", res.data.access);
            localStorage.setItem("refresh", res.data.refresh);
            props.history.push(Routes.Dashboard);
        })
        .catch(err => alert("Wrong Credentials"))
    }

    render(){
        return (
            <Col md={{span:4, offset: 4}} id="registerPanel">
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
                    <Form.Group>
                        <Form.Label>Name</Form.Label>
                        <Form.Control
                            type="text"
                            onChange={(e) => {this.setState({name: e.currentTarget.value})}}
                        />
                    </Form.Group>
                    <Form.Group>
                        <Form.Label>Surname</Form.Label>
                        <Form.Control
                            type="text"
                            onChange={(e) => {this.setState({suername: e.currentTarget.value})}}
                        />
                    </Form.Group>
                    <Form.Group>
                        <Form.Label>Customer/Veterinarian</Form.Label>
                        <Form.Control
                            as="select"
                            onChange={(e) => {this.setState({user_type: e.currentTarget.value})}}
                        >
                            <option value="veterinarian">Veterinarian</option>
                            <option value="customer">Customer</option>
                        </Form.Control>
                    </Form.Group>
                    <Button onClick={() => {this.register()}}>Register</Button>
                </Form>
            </Col>
        )
    }
} 