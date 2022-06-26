import React from 'react'
import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router';
import { Container, ContainerProfile, ContainerBorder, ContainerChild } from '../style/layoutStyled'
import { Title, SubTitle, BodyText,BodyTextBorder, CardAbout } from '../style/styledElements'

import axios from 'axios'


export const About = () => {
  //การใช้ axios จะทำให้เราได้ json data มาเลยโดยไม่ต้องใช้คำสั่งแปลง
  const [count, setCount] = useState(0)

  const [data, setData] = useState([]);

  //ทดสอบการใช้ axios ดึง json มาจากเว็บ portfolio สำหรับดึง api โดยเฉพาะ
  //แต่ตอนนีั้ยังไม่มีข้อมูลให้ดึง พักไว้ก่อน
  // useEffect(() =>{

  //   axios.get('https://gitconnected.com/v1/portfolio/pj-stone50')
  //     .then(res => setData(res.data));
    
  // },[])

  // console.log(data);


  return (

    


    <Container className="h-full">

      <Title>About this website</Title>
      <hr />
      {/* ---------------------------------------------------------- */}
    
      <SubTitle className="text-orange-400 p-3 mt-3">Development history</SubTitle>

      <ContainerChild className='grid grid-cols-3 items-center justify-center'>

        <CardAbout className='p-5 '>
          <SubTitle className="text-orange-300">Edited Saturday Night</SubTitle>
          <BodyText>4th June 2022</BodyText>
        </CardAbout>
        
        <CardAbout className='p-5'>
          <SubTitle className="text-orange-300">Edited Saturday Night</SubTitle>
          <BodyText>4th June 2022</BodyText>
        </CardAbout>
      
        <CardAbout className='p-5'>
          <SubTitle className="text-orange-300">Edited Sunday Night</SubTitle>
          <BodyText>12th June 2022</BodyText>
          
          <ul style={{alignItems:'top',listStyleType: 'none'}}>
            <p>สิ่งที่ขาด</p>
            <li>1.โปรเจคเก็บลง port</li>  
            <li>2.ผลงาน UX/UI design</li>
            <li>3.jason data จากเว็บที่จารโอมแนะนำ ใช้สำหรับทำเว็บ portfolio</li>
          </ul>  
        </CardAbout>

        <CardAbout className='p-5'>
          <SubTitle className="text-orange-300">Edited Friday Morning</SubTitle>
          <BodyText>17th June 2022</BodyText>
          
          <ul style={{alignItems:'top',listStyleType: 'none'}}>
            <p>สิ่งที่ขาด</p>
            <li>1.โปรเจคเก็บลง port</li>  
            <li>2.ผลงาน UX/UI design</li>
            <li>3.jason data จากเว็บที่จารโอมแนะนำ ใช้สำหรับทำเว็บ portfolio</li>
          </ul>  
        </CardAbout>

        <CardAbout className='p-5'>
          <SubTitle className="text-orange-300">Edited Sunday Afternoon</SubTitle>
          <BodyText>19th June 2022</BodyText>
          
          <ul style={{alignItems:'top',listStyleType: 'none'}}>
            <p>progress</p>
            <li>1.Home Background</li>  
            <li>2.Link to other pages</li>
            <li>3.</li>
          </ul>  
        </CardAbout>

        <CardAbout className='p-5'>
          <SubTitle className="text-orange-300">Edited Wednesday Afternoon</SubTitle>
          <BodyText>22th June 2022</BodyText>
          
          <ul style={{alignItems:'top',listStyleType: 'none'}}>
            <p>progress</p>
            <li>1.About Page</li>  
            <li>2.</li>
            <li>3.</li>
          </ul>  
        </CardAbout>
        
      </ContainerChild>

      <hr />
      {/* ---------------------------------------------------------- */}
    
      <SubTitle className="text-orange-400 p-3 mt-3">My Purpose</SubTitle>

      <ContainerChild className=' flex justify-center items-center'>
        <ContainerBorder className='max-w-6xl p-5'>
          
          <BodyText>The content of the website contains sound effects, atmosphere, music, for you to try and download.The content of the website contains sound effects, atmosphere, music, for you to try and download.</BodyText>
          <br />
          <BodyText>As many developers understand This website was created to train your website development skills to becoming a full-stack developer and to keep in your portfolio. It is open to anyone to download resources from this website for free. After this website is launched</BodyText>
        
        </ContainerBorder>
      </ContainerChild>
    

    </Container>
    
  )
}