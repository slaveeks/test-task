import React, {useState, useEffect} from 'react';
import styled from 'styled-components';
import Row from './Row';
import Column from './Column';
import {Transport} from '../../../transport/transport';

/**
 * Interface for table component props
 */
interface Props{
}

/**
 * Table component
 *
 * @param {Props} props - props of component
 *
 * @return {React.FC<Props>}
 */
const Table: React.FC<Props> = ({...props}) => {
  const [data, setData] = useState<Array<Array<string | number>> | null>(null);

  useEffect(() => {
    const exec = async (): Promise<void> => {
      // Data returns as array of lines, which consists array of columns' data
      const response = await Transport.getAllData();
      setData(response);
    };

    exec();
  }, []);
  return (
    <TableStyled {...props}>
      <thead>
        <Row isArticleRow={true}>
          <Column text={'№'}/>
          <Column text={'заказ №'}/>
          <Column text={'стоимость,$'}/>
          <Column text={'срок поставки'}/>
          <Column text={'стоимость,₽'}/>
        </Row>
      </thead>
      <tbody>
        { data ? data!.map((entity, index) =>
          <Row isArticleRow={false} key={index}>
            {entity.map((a, index) =>
              <Column text={a.toString()} key={index}/>,
            )}
          </Row>,
        ): null}
      </tbody>
    </TableStyled>
  );
};


/**
 * Styled table component
 *
 * @param props - props of component
 */
const TableStyled = styled.table<Props>`
  position: absolute;
  width: 100%;
  right: 0;
  top: 100px;
  border: 1px solid black;
  border-collapse: collapse;
`;

export default Table;
