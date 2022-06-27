import React, {useEffect, useState} from 'react';
import styled from 'styled-components';
import {Transport} from '../../../transport/transport';
import {TotalSum} from '../../../transport/types/TotalSum';

/**
 * Interface for container component props
 */
interface Props{
}

/**
 * Styled container component
 *
 * @param props - props of component
 */
const InfoStyled = styled.div<Props>`
  font-size: 25px;
  text-align: center;
  align-content: center;
  box-sizing: border-box;
  border-width: 0 1px 1px 1px;
  border-color: gray;
  border-style: solid;
`;

const ArticleStyled = styled.div<Props>`
  height: 20px;
  background-color: black;
  color: white;
  font-size: 19px;
  align-content: center;
  text-align: center;
`;

const TotalInfoContainerStyled = styled.div<Props>`
  width: 200px;
  height: 50px;
`;

/**
 * Container component
 *
 * @param {Props} props - props of component
 *
 * @return {React.FC<Props>}
 */
const TotalInfo: React.FC<Props> = ({...props}) => {
  const [data, setData] = useState<TotalSum | null>(null);

  useEffect(() => {
    const exec = async (): Promise<void> => {
      const response = await Transport.getSumOfOrders();
      console.log(response);
      setData(response);
    };

    exec();
  }, []);
  return (
    <TotalInfoContainerStyled {...props}>
      <ArticleStyled>
        Total
      </ArticleStyled>
      <InfoStyled>
        { data?.sum }
      </InfoStyled>
    </TotalInfoContainerStyled>
  );
};

export default TotalInfo;
