import React from 'react'
// import { Container, Card, Row, Col, Image, Button } from 'react-bootstrap'
import { Container,ContainerHome } from '../style/layoutStyled'
import { ButtonContent, Title, SubTitle, BodyText } from '../style/styledElements'
import { About } from './About'
import 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r121/three.min.js'
import 'https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.waves.min.js'
import { useState ,useEffect } from 'react'

import { ButtonLink } from '../style/styledElements'

import ReactLoading from 'react-loading';

const profile_pic = "https://i.pinimg.com/736x/fb/36/1b/fb361bf2f042a4e149a2adbd9bfbb6e5.jpg"

export const Home = () => {

  //Loading webpage
  const [loading, setLoading] = useState(false);

  
  useEffect(() => {
    setLoading(true);

    VANTA.WAVES({
    el: "#header-bg",
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.00,
    scaleMobile: 1.00,
    color: 0xf0f0f,
    waveHeight: 2.00,
    waveSpeed: 1.50,
    // zoom: 1.8
     }
    
    )

    setLoading(false)



  })
  
  

  return (
    
<>


    <Container className='h-full relative pt-0' style={{}}>



    
    {loading ? (
      <div className="h-screen flex justify-center">
        <ReactLoading type={"bubbles"} color={"#EEA753"} height={"15%"} width={"20%"}></ReactLoading>
      </div>
    ) : (
      <>
        <div className="home-content" id="header-bg" style={{backgroundColor:'none'}}>
        <ContainerHome >
          <Title>
            FREE DOWNLOAD
          </Title>

          <SubTitle>
            Sound Effect & Music
          </SubTitle>
            
            <br />

          <BodyText>
            Free Trial Music & Sound Effects with many more features you can try for free now.
          </BodyText>

          <BodyText>
            If you want to encourage the development of the website further. You can comment to give advice through the channels below. or <a href="#">support us</a>
          </BodyText>

          <br />

          <div className="btn-content">
            
              <ButtonLink to="/signin" className=" mr-8">
                <ButtonContent >Get Started</ButtonContent>
              </ButtonLink>

              <ButtonLink to="/signin" className=" mr-8">
                <ButtonContent style={{backgroundColor:'#868686'}}>Pricing</ButtonContent>
              </ButtonLink>
              
            

          </div>
        </ContainerHome>
      </div>
  
      <About/>
      
      </>
    )}
  
  
      
    </Container>
</>
  )
}



