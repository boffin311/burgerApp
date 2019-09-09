import React from 'react';  
import './modal.css';
import Aux from '../../../hoc/Aux';
import Backdrop from '../backdrop/backdrop';

export default function Modal(props) {
    return (
        <Aux>
            <Backdrop show={props.show}  clicked={props.modalClosed}/>
        <div className="Modal"
            style={{
                transform: props.show ? 'translateY(0)' : 'translateY(-100vh)',
                opacity: props.show ? '1' : '0' 
            }}>
            {props.children}
        </div>
        </Aux>
      
    )
}
