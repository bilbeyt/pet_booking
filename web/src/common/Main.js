import React from 'react';
import Header from '../common/Header';

export default class Main extends Component{
    render(){
        return (
            <div>
                <Header/>
                <main role="main" class="container">
                    <div class="jumbotron">
                        <h1>Navbar example</h1>
                        <p class="lead">This example is a quick exercise to illustrate how the top-aligned navbar works. As you scroll, this navbar remains in its original position and moves with the rest of the page.</p>
                        <a class="btn btn-lg btn-primary" href="https://getbootstrap.com/docs/4.5/components/navbar/" role="button">View navbar docs »</a>
                    </div>
                </main>
            </div>
        )
    }
}