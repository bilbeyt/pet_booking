import React from 'react';
import {Form, Button, Col, Row} from 'react-bootstrap';
import axios from 'axios';
import settings from '../../settings';

export default class CreateAppointment extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            pets: [],
            slots: [],
            purposes: [
                {'value': 'Vac', 'label': 'Vaccination'},
                {'value': 'Fol', 'label': 'Follow up'},
                {'value': 'Che', 'label': 'Checkup'},
            ],
            vaccines: [],
            books: []
        }
    }

    componentDidMount(){
        axios.get(`${settings.host}/api/appointment-slots/`).then(res => this.setState({slots: res.data}));
        axios.get(`${settings.host}/api/pets/`).then(res => {this.setState({pets: res.data})});
        axios.get(`${settings.host}/api/vaccine-types/`).then(res => {this.setState({vaccines: res.data})});
    }

    book(){
        const {pet, slot, purpose, vaccine_type, is_recurring, medical_history, reason} = this.state;
        axios.post(`${settings.host}/api/appointments/`, {pet, slot, purpose, vaccine_type, is_recurring, medical_history, reason})
        .then((res) => {this.setState({books: res.data})})
        .catch(() => {console.log('Fail')})
    }

    render(){
        const {pets, slots, purposes, purpose, vaccines, books} = this.state;
        if(!pets || !slots || !vaccines) return <div></div>
        const petOptions = pets.map((pet) => {return <option value={pet.id}>{pet.name} - {pet.owner.first_name}_{pet.owner.last_name}</option>})
        const purposeOptions = purposes.map((purpose) => {return <option value={purpose.value}>{purpose.label}</option>})
        const vaccineOptions = vaccines.map((vaccine) => {return <option value={vaccine.id}>{vaccine.description}</option>})
        const slotOptions = slots.map((slot) => {return <option value={slot.id}>{slot.checkin_time} - {slot.checkout_time} - {slot.veterinarian.user.first_name} - {slot.veterinarian.user.last_name}</option>})
        const booksDiv = books.map((book) => {
            return (
                <tr>
                    <td>{book.pet.name}</td>
                    <td>{book.purpose}</td>
                    <td>{book.slot.checkin_time}</td>
                    <td>{book.slot.checkout_time}</td>
                    <td>{book.is_recurring}</td>
                </tr>
            )
        })
        return (
            <Row>
                <Col md={{span: 4, offset:4}}>
                    <h1>Appointments</h1>
                    <Form>
                        <Form.Group>
                            <Form.Label>Pet</Form.Label>
                            <Form.Control 
                                as="select"
                                onChange={(e) => {this.setState({pet: e.currentTarget.value})}}>
                            <option value="-">---</option>
                            {petOptions}
                            </Form.Control>
                        </Form.Group>
                        <Form.Group>
                            <Form.Label>Slot</Form.Label>
                            <Form.Control
                                as="select"
                                onChange={(e) => {this.setState({slot: e.currentTarget.value})}}>>
                                <option value="-">---</option>
                                {slotOptions}
                            </Form.Control>
                        </Form.Group>
                        <Form.Group>
                            <Form.Label>Purpose</Form.Label>
                            <Form.Control
                                as="select"
                                onChange={(e) => {this.setState({purpose: e.currentTarget.value})}}>>
                                <option value="-">---</option>
                                {purposeOptions}
                            </Form.Control>
                        </Form.Group>
                        { purpose === 'Vac' ?
                        <div>
                            <Form.Group>
                                <Form.Label>Vaccine Type</Form.Label>
                                <Form.Control
                                    as="select"
                                    onChange={(e) => {this.setState({vaccine_type: e.currentTarget.value})}}>>
                                    <option value="-">---</option>
                                    {vaccineOptions}
                                </Form.Control>
                            </Form.Group>
                            <Form.Group>
                                <Form.Check 
                                    type="checkbox"
                                    label="Is recurring"
                                    onChange={(evt) => {this.setState({is_recurring: evt.target.checked })}}/>
                            </Form.Group>
                        </div> : null }
                        {purpose === 'Fol' ? 
                        <Form.Group>
                            <Form.Label>Medical History</Form.Label>
                            <Form.Control
                                as="textarea"
                                onChange={(e) => {this.setState({medical_history: e.currentTarget.value})}}
                            />
                        </Form.Group> : null
                        }
                        {purpose === 'Che' ? 
                        <Form.Group>
                            <Form.Label>Reason</Form.Label>
                            <Form.Control
                                as="textarea"
                                onChange={(e) => {this.setState({reason: e.currentTarget.value})}}
                            />
                        </Form.Group>
                        : null}
                        <Button onClick={(e) => this.book()}>Book</Button>
                    </Form>
                </Col>
                { books.length ?
                <Col md={4}>
                    <h1>Existing Appointments</h1>
                    <table className="table">
                        <thead>
                            <tr>
                                <th>Pet Name</th>
                                <th>Purpose</th>
                                <th>Checkin</th>
                                <th>Checkout</th>
                                <th>Recurring?</th>
                            </tr>
                        </thead>
                        <tbody>
                            {booksDiv}
                        </tbody>
                    </table>
                </Col> : null}
            </Row>
        )
    }
} 