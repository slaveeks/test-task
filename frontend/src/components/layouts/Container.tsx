import React from 'react';
import styled from 'styled-components';

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
const ContainerStyled = styled.div<Props>`
  position: absolute;
  height: 100vh;
  display: flex;
  top: 0;
  bottom: 0;
  left: 0;
  width: 100vw;
`;

/**
 * Container component
 *
 * @param {Props} props - props of component
 *
 * @return {React.FC<Props>}
 */
const Container: React.FC<Props> = ({...props}) => {
  return (
    <ContainerStyled {...props}/>
  );
};

export default Container;
