import axios from 'axios';
import React from 'react'
import { useState ,useEffect } from 'react';
import { Container } from '../style/layoutStyled'
import { Title, SubTitle, BodyText,Card } from '../style/styledElements'

import ReactLoading from 'react-loading';


export const Blog = () => {
  //get API article using axios
  const [posts, setPosts] = useState([]);
  //Loading webpage
  const [loading, setLoading] = useState(false);
  
  useEffect(() => {
    setLoading(true);
    axios.get('https://saurav.tech/NewsAPI/sources.json')
      .then(res => {
        //for getting api
        setPosts(res.data.sources);
        //for setting load
        setLoading(false);
      });

  }, []);

  console.log(posts)

  return (
    <>
      <Container className='h-full ml-24 mr-24'>
        <Title>Blog Page</Title>
        <hr />

          {loading ? (
            <div style={{ display: 'flex', justifyContent: 'center' }}>
              <ReactLoading type={"bubbles"} color={"#EEA753"} height={"15%"} width={"20%"}></ReactLoading>
            </div>
          ) : (
            <>
              {posts.map((data, idx) => (
              <>
                <div key={idx} className="p-4 text-left max-w-2xl">
                  <Card className='h-full'>
                    <h4>Name: {data.name}</h4>
                    <p>Description: {data.description}</p>
                    <p>Url: <a href={data.url} target="_blank">{data.url}</a></p>
                  </Card>
                </div>
                <hr />
              </>
            ))}
            </>
          )}
          
        


      </Container>
    </>
  )
}

