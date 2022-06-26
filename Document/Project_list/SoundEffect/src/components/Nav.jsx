import React from 'react'
import { useState,useEffect,useRef } from 'react'
import { NavBar,NavLogo,NavButton,NavText, NavMenu, NavList, NavLink, NavBtnLink, Bars, NavBtn } from '../style/styledElements'


function Nav() {

  const [show, setShow] = useState(false);
  console.log(show)

  return (
    <>
    
      <NavBar show={show}>
        <NavLogo className="logoFont" to='/'>
          ProfessSound
        </NavLogo>

        <Bars onClick={() => setShow(!show)} />

        <NavMenu show={show}>

          <NavList>
            <NavLink to="/home">HOME</NavLink>
          </NavList>
          
          <NavList>
            <NavLink to="/about">ABOUT</NavLink>
          </NavList>
          <NavList>
            <NavLink to="/contact">CONTACT</NavLink>
          </NavList>
         

          <NavList>
            <NavLink to="/sounds">Sounds</NavLink>
          </NavList>

          <NavList>
              <NavLink to="/blog">Blog</NavLink>
            </NavList>

          
        

          
          

        
          

          
        </NavMenu>

        <NavBtn>
          <NavBtnLink to="/signin">SIGN IN</NavBtnLink>
        </NavBtn>
        
      </NavBar>
    
    </>
  )
}

export default Nav