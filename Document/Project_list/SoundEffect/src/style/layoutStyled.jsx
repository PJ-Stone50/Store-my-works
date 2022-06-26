import styled from 'styled-components'



export const Container = styled.div `
  background: #161616;;
  // margin: 3rem;
  
  padding: 100px 0  100px 0;
`

export const ContainerProfile = styled.div`
  padding: 16px;
`




export const ContainerFooter = styled.div`
  width: 100%;
  /* padding: 1rem; */
  background-color: #EEA753;

  position: fixed;
  bottom: 0;

`

export const ContainerHome = styled.div`
  position: absolute;
  margin: auto;
  margin-top: 13rem;
  height: 100vh;
  width: 100%;
  

  padding: 2rem;

  @media screen and (max-width: 768px){
    margin-top: 3rem;
    max-width: 50rem;
    min-width: 500px;
  }

`


export const ContainerBorder = styled.div`
  // margin: 2rem 2rem 2rem  auto;
  // margin-left; 2rem;
  width: 100%;
  border: 2px solid #fff;
  border-radius: 25px;
  // padding: 3rem;
  // margin: 3rem;
`

export const ContainerChild = styled.div`
  background: #161616;;
  margin: 0;
  // padding: 1rem 0  1rem 0;
  padding: 0;
`