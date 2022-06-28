import React from 'react';
import styled from 'styled-components';

/**
 * Interface for container for orders info component props
 */
interface Props{
}

/**
 * Container for orders info component
 *
 * @param {Props} props - props of component
 *
 * @return {React.FC<Props>}
 */
const OrdersInfoContainer: React.FC<Props> = ({...props}) => {
  return (
    <OrdersInfoContainerStyled {...props}/>
  );
};


/**
 * Styled container for orders info component
 *
 * @param props - props of component
 */
const OrdersInfoContainerStyled = styled.div<Props>`
  display: block;
  position: absolute;
  align-items: center;
  padding-top: 30px;
  top: 0;
  right: 0;
  width: 600px;
  height: 100vh;
`;

export default OrdersInfoContainer;
