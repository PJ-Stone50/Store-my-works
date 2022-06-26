import { NavLink as Link } from 'react-router-dom'
import styled from 'styled-components'
import { FaBars } from 'react-icons/fa'

export const NavBar = styled.nav`
  display: flex;
  position: ${props => props.show ? 'flex' : 'absolute'};
  justify-content: center; 
  // height: 85px;
  height: ${props => props.show ? 'auto' : '85px'};
  background-color: ${props => props.show ? '#181818' : 'none'};
  // margin-bottom: ${props => props.show ? '20rem' : '0'};
  width: 100%;
  z-index: 10;
  `
export const NavLogo = styled(Link)`

  position: absolute;
  // margin: ${props => props.show ? '0' : 'auto'};
  margin: 0;
  // left: ${props => props.show ? '0' : '3rem'};
  left: 3rem;
  top: 1.25rem;
  color: #FFDF8D;
  font-style: normal;
  font-weight: 400;
  // font-size: ${props => props.show ? '28px' : '56px'};
  font-size: 28px;
  letter-spacing: 1.275px;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.5);
  // width: 100%;

  @media screen and (max-width: 768px){
    display: none;
  }

  &:hover{
    color: #FFDF8D;
  }
`

export const Bars = styled(FaBars)`
  display: none;
  color: #FFDF8D;
  // font-size: 10rem;
  margin: 1rem;

  @media screen and (max-width: 768px){
    display: block;
    position: absolute;
    top: 0;
    right: 0;
    transform: translate(-100%, 75%);
    font-size: 1.8rem;
    cursor: pointer;

    // height: auto;
    // min-height: 3rem;

  &.show {
    display: block;
    color: #fff;
  }

  }


  
`

export const NavMenu = styled.ul`
  
  display: flex;
  justify-content: space-around;
  align-items: center;
  
  height: auto;
  width: 100%;
  max-width: 720px;
  // white-space: nowrap;
  
  @media screen and (max-width: 1200px) {
    // display: none;
    display: ${props => props.show ? 'block' : 'none'}
  }
`

export const NavList = styled.li`
  display: flex;
  aligm-items: center;
  padding 0;
  cursor: pointer;
  justify-content: center;


  @media screen and (max-width: 768px) {
    padding: 2rem 0;
  }
`

export const NavBtn = styled.nav`
  display: flex;
  align-items: center;
  margin-right: 24px;

  @media screen and (max-width: 1200px) {
    display: none;
  }
`

export const NavBtnLink = styled(Link)`
  position: absolute;
  right: 3rem;
  top: 1rem;
  font-size: 1.25em;

  border-radius: 4px;
  background: #FFDF8D;;
  padding: 10px 22px;
  color: #000000;
  border: none;
  outline:none;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  text-decoration: none;

  &:hover{
    transition: all 0.2s ease-in-out;
    color: #000000;
  }

  
`

export const NavLink =styled(Link)`
  font-size: 1.25em;
  color: #fff;
  

  transition: transform .3s ease-out;
  // display: inline-block; ทำให้ NavBar absolute Error

  opacity: 0.8;

  &.active{
    color: #fff;
    opacity: 1;
  }

  &:hover{
    color: #fff;
    //CSS3
    transform: translate(0%, -5px);
  }
  
`
export const ButtonLink =styled(Link)`
  :hover{
    color: #000000;
  }
  
`


export const Title = styled.h1`
  font-style: normal;
  font-weight: 400;
  font-size: 84px;
  letter-spacing: 1.275px;
  text-aligns:center;
  align-items:center;
  justify-content: center;
`

export const SubTitle = styled.h2`
  font-style: normal;
  font-weight: 400;
  font-size: 45px;
  letter-spacing: 1.275px;
`

export const BodyText = styled.p`
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  letter-spacing: 1.275px;

`

export const BodyTextBorder = styled.p`
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  letter-spacing: 1.275px;
  border: 3px solid #fff;
`

export const ButtonContent = styled.button`
  display: inline-block;
  position: relative;
  overflow: hidden;
  text-decoration: none;

  padding: 0 20px;
  align-items: center;
  justify-content: center;
  height: 3em;
  background: #EEA753;
  color: #000000;
  border-radius: 30px;
  margin: 1rem;

  @media screen and (max-width: 768px){
    margin: 0.5rem;
  }

    &:after {
      content: '';
      // width: 20%;
      height: 100%;
      // position: absolute;
      left: auto;
      top: 0;
      bottom: 0;
      right: -20%;
      background-image: 
        linear-gradient(135deg, 
          rgba(255,255,255,0),
          rgba(255,255,255,.8),
          rgba(255,255,255,0)
        );
    }
    &:hover {

      &:after {
      transition: all .4s ease-out;
        right: 100%;
      }
    }
  }
`

export const NavButton = styled.button`
  width: 168px;
  height: 41px;

  background: #EEA753;
  border-radius: 15px;
`

export const NavText = styled.a`
  font-size: 24px;
  color: #000000;
`

export const CardAbout = styled.div`
  margin: 2rem auto;
  width: 100%;
  border: 2px solid #fff;
  border-radius: 25px;
  max-width: 500px;
  max-height: 700px;
`

export const Card = styled.div`
  margin: 2rem auto;
  width: 100%;
  border: 2px solid #fff;
  border-radius: 25px;
  
`

export const FooterContainer = styled.div`
  text-align: center;

  background-color: #121212;
  padding: 5rem;
  width: 100%;
  

`