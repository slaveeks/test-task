import React, {PropsWithChildren} from 'react';
import styled, {css} from 'styled-components';

/**
 * Interface for container component props
 */
interface Props extends PropsWithChildren{
  isArticleRow: boolean;
  key: string;
}

/**
 * Container component
 *
 * @param {Props} props - props of component
 *
 * @return {React.FC<Props>}
 */
const Row: React.FC<Props> = (props) => {
  return (
    <RowStyled {...props}/>
  );
};

/**
 * Styled container component
 *
 * @param {Props} props - props of component
 * @return {css}
 */
const RowStyled = styled.tr<Props>`
  border: 1px solid black;
  width: 100px;
  background-color: aqua;
  text-align: right;
  ${(props) => props.isArticleRow && css`
    height: 50px;
    text-align: center;
    background-color: black;
    color: azure;
  `}
`;

export default Row;
