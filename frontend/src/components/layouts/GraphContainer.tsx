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
  height: 500px;
  top: 10px;
  left: 0;
  width: 800px;
`;

/**
 * Container component
 *
 * @param {Props} props - props of component
 *
 * @return {React.FC<Props>}
 */
const GraphContainer: React.FC<Props> = ({...props}) => {
  return (
    <ContainerStyled {...props}/>
  );
};

export default GraphContainer;
