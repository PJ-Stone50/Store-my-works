import React, { useState } from 'react'
import { Container, Row, Col, Image, Button, Form, Alert } from 'react-bootstrap'

import { CardAbout }  from '../style/styledElements'
export const Contact = () => {

  



  


  return (
    <Container className="h-screen flex justify-center pt-24 w-84">
      <CardAbout className="">
        <Form.Floating>
          <h1>Contact Me</h1>

          <Form.Group>
            <Form.Label className="mt-3">Name</Form.Label>
            <Form.Control
              type="text"
              name="name"
              placeholder="Enter your name"
              // value={name}
              // onChange={handleChange}
            />

          </Form.Group>

          <Form.Group>
            <Form.Label className="mt-3">Email</Form.Label>
            <Form.Control
              type="email"
              name="email"
              placeholder="Enter your email"
              // value={email}
              // onChange={handleChange}
            />

          </Form.Group>

          <Form.Group>
            <Form.Label className="mt-3">Message</Form.Label>
            <Form.Control
              as="textarea"
              name="message"
              placeholder="Enter your message"
              // value={message}
              // onChange={handleChange}
            />

          </Form.Group>
          {/* onClick เมื่อกดปุ่มให้ set เป็น true */}
          <Button variant='primary' className="mt-3" type="submit" onClick={() => setShow(true)}>Submit</Button>

        </Form.Floating>

        <Alert className="mt-3 w-full" variant="success">
          Your message has been sent!
        </Alert>

      </CardAbout>
    </Container>
  )
}